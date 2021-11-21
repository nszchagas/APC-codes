QTD_AMIGOS = 4
celulares = dict() #keys = modelo, values = [preco, qtd_no_grupo]
PRECO, QTD_NO_GRUPO = 0, 1

for x in range(QTD_AMIGOS):
  input()
  modelo = input()
  preco = int(input())
  if modelo in celulares.keys():
    celulares[modelo][QTD_NO_GRUPO] += 1
    if preco < celulares[modelo][PRECO]:
      celulares[modelo][PRECO] = preco
  else: 
    celulares[modelo] = [preco, 1]

def getModelos(quantidade):
  modelos = []
  for modelo in celulares:
    if celulares[modelo][QTD_NO_GRUPO] == quantidade:
      modelos.append(modelo)
  return modelos

def getPopulares():
  modelosOrdenados = sorted(celulares.values(), key= lambda x : x[QTD_NO_GRUPO], reverse=True)
  return getModelos(modelosOrdenados[0][-1])

def getMaisBarato(modelos):
  maisBarato = ''
  if len(modelos) == 1:
    return modelos[0]
  else: 
    menor_preco = 40001
    for modelo in modelos:
      if celulares[modelo][PRECO] < menor_preco:
        maisBarato = modelo
        menor_preco = celulares[modelo][PRECO]
  return maisBarato

populares = getPopulares()
if len(populares) == 1:
  print(populares[0])
else:
  print(getMaisBarato(populares))
