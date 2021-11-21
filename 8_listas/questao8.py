
qtd = int(input())
numeros = list(map(int, input().strip().split(' ')))
VALOR = 42
numeros.sort()


def verificaSoma(numeros, VALOR):
  for i in range(len(numeros)):
    for j in range(i, len(numeros)):
      if numeros[i]+numeros[j] == VALOR:
        return "sim"
  return "nao"


print(verificaSoma(numeros))