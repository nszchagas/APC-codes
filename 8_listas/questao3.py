rede = []
peixe = ''

while peixe != 'acabou':
  peixe = input()
  if peixe != 'acabou':
    rede.append(peixe)

print("Hoje eu pesquei:")
for p in rede:
  print(p)