nota1, qtd1 = input().split()
nota2, qtd2 = input().split()

qtd1 = int(qtd1)
qtd2 = int(qtd2)

ORDEM = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']
if nota1 in ORDEM and nota2 in ORDEM:
  if ORDEM.index(nota1.lower()) < ORDEM.index(nota2.lower()):
    primeira = nota1
    segunda = nota2
  else:
    primeira = nota2
    segunda = nota1
else:
  if nota1 < nota2:
    primeira = nota1
    segunda = nota2
  else: 
    primeira = nota2
    segunda = nota1

if qtd1 > qtd2: 
  sozinha = nota1
else: 
  sozinha = nota2
 
qtd_comum = min(qtd1, qtd2)
qtd_sozinha = abs(qtd1 - qtd2)
print(qtd_comum*(primeira+segunda)+qtd_sozinha*sozinha)

