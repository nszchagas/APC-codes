
mesas = dict()
cardapio = dict()
estoque = dict()
areas = []
pedidos = [] #lista de dicts

## FUNÇÕES GERAIS ##

def listToDict(lista):
  dicionario = {item: 0 for item in lista}
  for item in lista:
    dicionario[item] = lista.count(item)
  return dicionario

def refresh(newMesas=None, newCardapio=None, newEstoque=None):
  global mesas, cardapio
  if newMesas != None:
    mesas.update(newMesas)
  if newCardapio != None:
    cardapio.update(newCardapio)
  if newEstoque != None:
    estoque.update(newEstoque)
  areas.sort()

def getMesasIDByArea(areaEscolhida):
  mesasArea = []
  for mesa in mesas:
    if mesas[mesa]['area'] == areaEscolhida:
      mesasArea.append(mesa)
  return sorted(mesasArea)

def isMesa(id):
  try: 
    if mesas[id]['status'] == 'ocupada':
      return [True, '']
    else:
      return [False, f'erro >> mesa {id} desocupada']
  except KeyError:
    return [False, f'erro >> mesa {id} inexistente']

def existemIngredientes(prato):
  try:
    for ingrediente in cardapio[prato]['ingredientes']:
      if ingrediente in estoque.keys():
        if cardapio[prato]['ingredientes'][ingrediente] > estoque[ingrediente]:
          return [False, f'erro >> ingredientes insuficientes para produzir o item {prato}']
      else: 
        return [False, f'erro >> ingredientes insuficientes para produzir o item {prato}']
    return [True, '']
  except KeyError:
    return [False, f'erro >> item {prato} nao existe no cardapio']

def preparaPrato(prato):
  ingredientes = cardapio[prato]['ingredientes']
  newEstoque = estoque.copy()
  for ingrediente in ingredientes: 
    newEstoque[ingrediente] -= 1
  refresh(newEstoque=newEstoque)

def getPedidosMesa(idMesa):
  pedidosMesa = []
  for pedido in pedidos: 
    if pedido['mesa'] == idMesa:
      pedidosMesa.append(pedido)
  return sorted(pedidosMesa, key = lambda d:d['prato'])

def getMesasComPedido():
  mesasId = []
  for pedido in pedidos:
    if pedido['mesa'] not in mesasId:
      mesasId.append(pedido['mesa'])
  return sorted(mesasId)

## FUNÇÕES ESPECÍFICAS ##



def atualizaMesas():
  filePath = input()
  newMesas = dict()
  with open(filePath, 'r', encoding='utf-8') as arquivo: 
    for linha in arquivo:
      numeroMesa, area, status = linha.strip().split(', ')
      newMesas[int(numeroMesa)] = {'area': area, 'status': status}
      if area not in areas:
        areas.append(area)
  refresh(newMesas=newMesas)

def atualizaCardapio(): 
  filePath = input()
  newCardapio = dict()
  with open(filePath, 'r', encoding='utf-8') as arquivo: 
    for linha in arquivo:
      prato, *ingredientes = linha.strip().split(', ')
      newCardapio[prato] = {'nome': prato, 'ingredientes': listToDict(sorted(ingredientes))}
  refresh(newCardapio=newCardapio)

def atualizaEstoque():
  filePath = input()
  
  with open(filePath, 'r', encoding='utf-8') as arquivo: 
    for linha in arquivo:
      ingrediente, qtd = linha.strip().split(', ')
      qtd = int(qtd)
      if ingrediente in estoque.keys():
        estoque[ingrediente] += qtd
      else:
        estoque[ingrediente] = qtd
  

def fazPedido():
  idMesa, prato = input().split(', ')
  idMesa = int(idMesa)
  buscaMesa = isMesa(idMesa)
  buscaIngredientes = existemIngredientes(prato)
  if buscaMesa[0] and buscaIngredientes[0]:
    print(f'sucesso >> pedido realizado: item {prato} para mesa {idMesa}')
    pedidos.append({'mesa': idMesa, 'prato': prato})
    preparaPrato(prato)
  else:
    if not buscaMesa[0]: 
      print(buscaMesa[-1])
    elif not buscaIngredientes[0]:
      print(buscaIngredientes[-1])


def imprimeRelatorioMesas():
  status = 'status'
  if len(areas) < 1:
    print('- restaurante sem mesas')
  else:
    for area in areas: 
      print(f'area: {area}')
      idMesas = getMesasIDByArea(area)
      if len(idMesas) < 1: 
        print('- area sem mesas')
      else:
        for id in idMesas:
          print(f'- mesa: {id}, status: {mesas[id][status]}')


def imprimeRelatorioCardapio():
  nome, ingredientes = 'nome', 'ingredientes'
  if len(cardapio.keys()) < 1:
    print('- cardapio vazio')
  else:
    for item in sorted(cardapio.keys()):
      print(f'item: {cardapio[item][nome]}')
      for ingrediente in cardapio[item]['ingredientes']:
        print(f'- {ingrediente}: {cardapio[item][ingredientes][ingrediente]}')



def imprimeRelatorioEstoque():
  estoqueVazio = True
  if len(estoque.keys()) >= 1:
    for ingrediente in sorted(estoque.keys()):
      if estoque[ingrediente] > 0:
        estoqueVazio = False
        print(f'{ingrediente}: {estoque[ingrediente]}')
  if len(estoque.keys()) == 0 or estoqueVazio:
    print('- estoque vazio')

def imprimeRelatorioPedidos():
  if len(pedidos) > 0:
    prato = 'prato'
    for id in getMesasComPedido():
      print(f'mesa: {id}')
      for pedido in getPedidosMesa(id):
        print(f'- {pedido[prato]}')
  else: 
    print('- nenhum pedido foi realizado')

def fechaRestaurante():
  if len(pedidos) < 1: 
    print('- historico vazio')
  else:
    for indice in range(len(pedidos)):
      mesa, pedido = 'mesa', 'prato'
      print(f'{indice+1}. mesa {pedidos[indice][mesa]} pediu {pedidos[indice][pedido]}')
      
  print('=> restaurante fechado')


def getComando(): 
  comando = ''
  print('=> restaurante aberto')
  while comando != '+ fechar restaurante':
    comando = input()
    if comando == '+ atualizar mesas':
      atualizaMesas()
    elif comando == '+ atualizar cardapio':
      atualizaCardapio()
    elif comando == '+ atualizar estoque':
      atualizaEstoque()
    elif comando == '+ fazer pedido':
      fazPedido()
    elif comando == '+ relatorio mesas':
      imprimeRelatorioMesas()
    elif comando == '+ relatorio cardapio':
      imprimeRelatorioCardapio()
    elif comando == '+ relatorio estoque':
      imprimeRelatorioEstoque()
    elif comando == '+ fechar restaurante':
      fechaRestaurante()
    elif comando == '+ relatorio pedidos':
      imprimeRelatorioPedidos()
    else:
      print('erro >> comando inexistente')

getComando()

