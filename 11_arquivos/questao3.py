filePath = input().strip()

with open(filePath, 'r', encoding='utf-8') as chamada: 
  aulas = chamada.readlines()

presencas = []

for dia in aulas: 
  presencas.extend(dia.replace('\n', '').split(','))

def getPresencas():
  naoRepetidos = []
  for nome in presencas:
    if nome not in naoRepetidos: 
      naoRepetidos.append(nome)
  return {aluno : presencas.count(aluno)/len(aulas) for aluno in naoRepetidos}

def getReprovados():
  reprovados = []
  for aluno in getPresencas():
    if getPresencas()[aluno] < 0.75:
      reprovados.append(aluno)
      print(aluno, end=' ')
  if len(reprovados) == 0:
    print('Nenhum aluno reprovado por faltas')
    

getReprovados()