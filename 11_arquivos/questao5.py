#filePath = input().strip()
filePath = 'p.txt'
PRINCESA, CAVALEIRO, DRAGAO = 'P', 'C', 'D'
with open(filePath, 'r', encoding='utf-8') as castelo:
  torre = castelo.readlines()

for i in range(len(torre)):
  if PRINCESA in torre[i]: 
    locPrincesa = int((len(torre) - i)/2)
    print(f'Princesa no andar {locPrincesa}')
  if CAVALEIRO in torre[i]: 
    locCavaleiro = int((len(torre) - i)/2)
    print(f'Cavaleiro no andar {locCavaleiro}')
  if DRAGAO in torre[i]: 
    locDragao = int((len(torre) - i)/2)
    print(f'Dragão no andar {locDragao}')


movCavaleiro, movDragao = [], []

for x in range(locPrincesa - locCavaleiro + 1):
  movCavaleiro.append(locCavaleiro + x)
  movDragao.append(locDragao + 2*x)

def cavaleiroGanha():
  for i in range(len(movCavaleiro)): 
    if movCavaleiro[i] == movDragao[i]:
      return False
  return True

if cavaleiroGanha(): 
  print('Quero ver descerem u.u')
else: 
  print('Mais um pro lanche!')
  
  




