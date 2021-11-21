import csv 

filePath = input().strip()

nomesFornecedores = []
itens = []

def getKey(valor, dicionario):
  for key in dicionario:
    if dicionario[key] == valor:
      return key
  return -1

with open(filePath, 'r', encoding='utf-8') as orcamentos: 
  leitor = csv.reader(orcamentos)

  for linha in leitor: 
    if leitor.line_num == 1: 
      qtdFornecedores, qtdItens = map(int, linha[0].split(' '))
      nomesFornecedores = linha[1:]
    else: 
      itemAtual = dict()
      itemAtual['nome'] = linha[0]
      for i in range(qtdFornecedores):
        itemAtual[nomesFornecedores[i]] = float(linha[i+1])
      itens.append(itemAtual)

for item in itens: 
  print(item['nome'], end=' ')

  valores = list(item.values())
  valores.remove(item['nome'])
  valores.sort()
  #print(valores)
  print(getKey(valores[0], item))
