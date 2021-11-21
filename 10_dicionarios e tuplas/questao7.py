tamanho = int(input())
lista = list(map(int, input().strip().split(' ')))
vetor = {
  i : lista[i] for i in range(tamanho)
}

qtd_perguntas = int(input())


def getPosicao(numero, dicionario):
  for key in dicionario:
    if dicionario[key] == numero:
      return key
  return -1

def count(numero, dicionario):
  qtd = 0
  for key in dicionario:
    if dicionario[key] == numero:
      qtd += 1
  if qtd > 0:
    return qtd
  else: 
    return -1

for x in range(qtd_perguntas):
  opcao, numero = map(int, input().strip().split(' '))
  if opcao == 1:
    print(count(numero, vetor))

  elif opcao == 2:
    print(getPosicao(numero, vetor))

