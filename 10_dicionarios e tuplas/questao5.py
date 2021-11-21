import itertools

def getDuplicates(list1, list2):
  return list(set(list1) & set(list2))

def mergeLists(list1, list2): 
  return list1 + list(set(list2) - set(list1))

def getSublists(lista, size):
  return list(itertools.combinations(set(lista), size))


qtd_alunos, qtd_pares = map(int, input().strip().split(' '))
nomes = input().strip().split(' ')
nomes.sort()
turma = { aluno: [] for aluno in nomes } 

  
for x in range(qtd_pares):
  amigo1, amigo2 = input().strip().split(' ')
  turma[amigo1].append(amigo2)
  turma[amigo2].append(amigo1)

for amigo1, amigo2 in getSublists(nomes, 2):
  amigos_comuns = getDuplicates(turma[amigo1], turma[amigo2])
  amigos_juntos = []
  if len(amigos_comuns) >= 1:
    for amigo_comum in amigos_comuns:
      amigos_juntos = mergeLists(turma[amigo1], turma[amigo2])
      amigos_juntos = mergeLists(amigos_juntos, turma[amigo_comum])
      turma[amigo1], turma[amigo2], turma[amigo_comum] = amigos_juntos[:], amigos_juntos[:], amigos_juntos[:]


for aluno in turma: 
  if aluno in turma[aluno]:
    turma[aluno].remove(aluno)
  print(f'{aluno} possui {len(set(turma[aluno]))} amigos')


