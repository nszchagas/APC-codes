s = input()

def findall(string, character): 
  indexes = []
  for i in range(len(string)): 
    if string[i] == character:
      indexes.append(i)
  return indexes

def caminhoPossivel(tesouro, pericles, barreiras):
  for i in barreiras: 
    if pericles < i and tesouro > i or pericles > i and tesouro < i:
      return False 
  return True

pos_tesouro = s.find('X')
pos_pericles = s.find('P')
posicoes_barreiras = findall(s, '#')
if 'X' not in s:
  print("Péricles, não tem tesouro")
elif caminhoPossivel(pos_tesouro, pos_pericles, posicoes_barreiras):
  print(f"Péricles, {pos_tesouro-pos_pericles} passos")
else: 
  print("Péricles esse caminho não funciona")


