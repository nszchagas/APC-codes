QTD_ITEMS = 5
verso = dict()
reverso = dict()

for i in range(QTD_ITEMS):
  chave = input()
  valor = int(input())
  verso[chave] = valor

for chave in verso: 
  reverso[verso[chave]] = chave

print(verso)
print(reverso)