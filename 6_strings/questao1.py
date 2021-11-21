def get_maior_menor(a, b): 
  if len(a) > len(b):
    maior = a
    menor = b
  else: 
    maior = b
    menor = a
  return [maior, menor]
  
def chars_comuns(maior, menor):
  chars_comuns = []
  for x in menor: 
    if maior.count(x) > 0:
      chars_comuns.append(x)
  return chars_comuns

def corta_strings(maior, menor, repetidos):
  i = 0
  while maior[i] != menor[i] and i < min(len(maior), len(menor)):
    if maior[i] not in repetidos: 
      maior = maior[i+1:]
    if menor[i] not in repetidos: 
      menor = menor[i+1:]
    i += 1
  return [maior, menor]

def corta_final(a, b):
  maior, menor = get_maior_menor(a, b)
  i = -2
  while menor not in maior and -i < min(len(maior), len(menor)): 
    menor[:-i] 
    i -= 1
    maior, menor = get_maior_menor(maior, menor)
  return [maior, menor]
  


 

a = input()
b = input()
operacoes = 0
maior, menor = get_maior_menor(a, b)
repetidos = chars_comuns(maior, menor)

if len(repetidos) == 0:
  operacoes = len(menor) + len(maior)
elif menor in maior: 
  operacoes = len(maior) - len(menor)


print(corta_final(corta_strings(maior, menor, repetidos)[0], corta_strings(maior, menor, repetidos)[1]))

