comprimento = int(input())
genoma = input()

#A quantidade de cada nucleotídeo A, C, G, T deve ser igual.

qtd_nucleotideos = [genoma.count('A'), genoma.count('C'), genoma.count('G'), genoma.count('T')]
qtd_desconhecida = genoma.count('?')

qtd_nucleotideos.sort(reverse=True)
if comprimento < 8 and qtd_nucleotideos[0]*4 == comprimento: 
  print('Segredos desvendados')  
elif comprimento >= 8 and comprimento % 4 ==0:
  print('Segredos desvendados')
elif qtd_desconhecida == comprimento and comprimento % 4 == 0:
    print('Segredos desvendados')
else:
  print('Feiticeiro misterioso')