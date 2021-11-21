tamanho = int(input())
vetor = tuple(map(int, input().strip().split(' ')))
qtd_bonitos = 0

def getPairs(vetor):
  duplas = []
  for x in range(len(vetor)):
    for y in range(x+1, len(vetor)):
      duplas.append((vetor[x], vetor[y]))
  return duplas

def isParBonito(par):
  return (par[0] == par[1]/2) or (par[1] == par[0]/2)

for par in getPairs(vetor):
  if isParBonito(par):
    qtd_bonitos += 1

print(qtd_bonitos)
