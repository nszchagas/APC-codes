filePath = input().strip()
qtdPedro, qtdFatorialPedro = 0, 0

with open(filePath, 'r', encoding='utf-8') as arquivo: 
  content = arquivo.readlines()

k = int(content[0].strip())
vetor = list(map(int, content[1].strip().split(' ')))

def getSegmentos(vetor, tamanho):
  listaSegmentos = []
  for i in range(len(vetor)-tamanho+1):
    listaSegmentos.append(vetor[i:i+k])
  return listaSegmentos

def isBonitoPedro(segmento, k):
  return sorted(segmento)[-1] >= 2*k

def isBonitoFatorialPedro(segmento, k):
  return sorted(segmento)[0] <= k/2

for segmento in getSegmentos(vetor, k):
  if isBonitoPedro(segmento, k):
    qtdPedro += 1
  if isBonitoFatorialPedro(segmento, k):
    qtdFatorialPedro += 1

print(f'{qtdPedro} {qtdFatorialPedro}')






