numeros = list(map(int, input().strip().split(' ')))
valor = int(input())
import itertools 


def ePossivelQtdValores(tamanho):
  dados = itertools.combinations(numeros, tamanho)
  sublistas = list(dados)
  for lista in sublistas: 
    soma = 0
    for item in lista: 
      soma += item
    if soma == valor:
      return True
  return False


def ePossivelLista():
  for qtdValores in range(len(numeros)):
    if ePossivelQtdValores(qtdValores):
      return 'E possivel ganhar.'
  return 'Impossivel ganhar.'

print(ePossivelLista())





