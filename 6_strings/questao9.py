casos = int(input())
for x in range(casos):
  entrada = input()
  qtd_um = entrada.count('1')
  if qtd_um > 0:
    if '1'*qtd_um not in entrada:
      primeiro_um = entrada.index('1') 
      ultimo_um = len(entrada) - 1 - entrada[::-1].index('1')
      qtd_apagados = entrada[primeiro_um:ultimo_um].count('0')
    else:
      qtd_apagados = 0
  else: 
    qtd_apagados = 0
  print(qtd_apagados)
      
