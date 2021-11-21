## VARIÁVEIS GLOBAIS ##
areas = [] 
NOME_AREA, MESAS, QTD_CADEIRAS, CADEIRAS_OCUPADAS, TEMPO_ATE_VAZIA = 0, 1, 0, 1, -1
# areas = [[nome_da_area, mesas]], com mesas = [qtd_cadeiras, tempo_ate_vazia]
visitantes = 0
## FUNÇÕES GERAIS ##

def getComando(): 
  for area in areas: 
    for mesa in area[MESAS]:
      if mesa[TEMPO_ATE_VAZIA] > 0:
        mesa[TEMPO_ATE_VAZIA] -= 1 
      if mesa[TEMPO_ATE_VAZIA] == 0:
        mesa[CADEIRAS_OCUPADAS] == 0      
  return input().strip()

def addMesasArea(nomeArea, qtd_mesas, lugares):
  mesas = []
  tempo_ate_vazia, cadeiras_ocupadas = 0, 0
  for x in range(qtd_mesas):
    mesas.append([lugares,cadeiras_ocupadas, tempo_ate_vazia])
  if not any (nomeArea in sublista for sublista in areas):
    areas.append([nomeArea, mesas])
  else: 
    for area in areas: 
      if area[NOME_AREA] == nomeArea: 
        area[MESAS].extend(mesas)


def removeMesas(qtd_mesas, lugares, area):
  mesas = getMesasArea(area)
  for x in range(qtd_mesas):
    mesas.remove([lugares, 0, 0]) #só serão removidas mesas vazias
  alteraArea(area, mesas)

def getMesasArea(area_escolhida): 
  mesas = []
  for area in areas:
    if area[NOME_AREA] == area_escolhida: 
      mesas = area[MESAS]
  return mesas

def alteraArea(area, alteracaoMesas):
  for area in areas: 
    if area[NOME_AREA] == area: 
      area[MESAS] = alteracaoMesas

def getIndexMesa(qtd_pessoas, area):
  mesas = sorted(getMesasArea(area),  key= lambda x:x[QTD_CADEIRAS])
  for mesa in mesas: 
    if mesa[QTD_CADEIRAS] >= qtd_pessoas and mesa[TEMPO_ATE_VAZIA] == 0:
      return getMesasArea(area).index(mesa)
  return -1

def printMesasArea(area):
  mesas = [item[0] for item in getMesasArea(area)]
  itens_unicos = []

  for qtd_lugares in sorted(mesas): 
    if qtd_lugares not in itens_unicos: 
      itens_unicos.append(qtd_lugares)
  for i in range(len(itens_unicos)):
    print(f' {mesas.count(itens_unicos[i])} mesas de {itens_unicos[i]} cadeiras.')
   

## CONFIGURAÇÃO ## 

def fazConfiguracao(): 
  entrada = ''
  while entrada != '--ATENDIMENTO':
    entrada = input()
    if entrada != '--ATENDIMENTO':
      nome, qtd_mesas, lugares = entrada.split(' ')
      qtd_mesas, lugares = int(qtd_mesas), int(lugares)
      addMesasArea(nome, qtd_mesas, lugares)

## ATENDIMENTO - COMANDO 1 - ESCOLHER MESA ## 

def escolheMesa():
  global visitantes
  entrada = input().split(' ')
  qtd_pessoas, area = int(entrada[4]), entrada[-1]
  indice = getIndexMesa(qtd_pessoas, area)
  if indice != -1:
    mesas = getMesasArea(area)
    mesas[indice][TEMPO_ATE_VAZIA] = qtd_pessoas*2 + 2
    mesas[indice][CADEIRAS_OCUPADAS] = qtd_pessoas
    alteraArea(area, mesas)
    visitantes += qtd_pessoas
    print(f'Um grupo de {qtd_pessoas} pessoas ocupou uma mesa de {mesas[indice][QTD_CADEIRAS]} lugares na area {area}.') 
  else:
    print(f'Nao foi possivel levar o grupo de clientes para uma mesa.')

## ATENDIMENTO - COMANDO 2 - IMPRIMIR MESAS (MESAS OCUPADAS POR ÁREA) ## 

def printMesas(): 
  areas_ordenadas = sorted(areas, key = lambda x:x[NOME_AREA])
  for area in areas_ordenadas:
    ocupadas = 0
    total = 0
    print(f'{area[NOME_AREA]}: ', end='')
    for mesa in getMesasArea(area[NOME_AREA]):
      total += 1
      if mesa[TEMPO_ATE_VAZIA] > 0:
        ocupadas += 1
    print(f'({ocupadas} de {total} mesas)') 

## ATENDIMENTO - COMANDO 3 - IMPRIMIR LOTAÇÃO (PESSOAS POR ÁREA) ## 

def printLotacao(): 
  areas_ordenadas = sorted(areas, key = lambda x:x[NOME_AREA])
  for area in areas_ordenadas: 
    ocupadas = 0
    total = 0
    print(f'{area[NOME_AREA]}: ', end='')
    for mesa in area[MESAS]: 
      total += mesa[QTD_CADEIRAS]
      if mesa[TEMPO_ATE_VAZIA] > 0:
        ocupadas += mesa[CADEIRAS_OCUPADAS]
      
    print(f'({ocupadas} de {total} pessoas)')

## ATENDIMENTO - COMANDO 4 - ALTERAR MESA ## 

def alteraMesas():
  entrada = input().split(' ')
  qtd_mesas, lugares = int(entrada[3]), int(entrada[6])
  operacao, area = entrada[1], entrada[-1]
 
  if operacao.lower() == 'adicionar': 
    addMesasArea(area, qtd_mesas, lugares)
    operacao_feita = 'adicionadas'
  

  elif operacao.lower() == 'remover': 
    operacao_feita = 'removidas'
    removeMesas(qtd_mesas, lugares, area)
  print( f'{qtd_mesas} mesas de {lugares} cadeiras {operacao_feita} com sucesso na area {area}.')

## ATENDIMENTO - COMANDO -1 - FECHAR RESTAURANTE ## 

def fechaRestaurante():
  print('Restaurante fechado.')
  print('Balanco final de mesas:')
  for area in sorted(areas, key=lambda x:x[NOME_AREA]): 
    print(f'{area[NOME_AREA]}:')
    printMesasArea(area[NOME_AREA])
  print(f'Um total de {visitantes} pessoas visitaram o restaurante hoje.')
  print('Bom descanso!')

## MENU PRINCIPAL ## 

def menuPrincipal(): 
  entrada = ''
  while (entrada != '-1'):
    entrada = getComando()
    if entrada == '--CONFIGURACAO':
      fazConfiguracao()
    elif entrada == '1':
      escolheMesa()
    elif entrada == '2':
      printMesas()
    elif entrada == '3':
      printLotacao()
    elif entrada == '4':
      alteraMesas()   
  fechaRestaurante()

menuPrincipal()