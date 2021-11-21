entrada = input()

alfabeto = {letra : entrada.count(letra) for letra in 'abcdefghijklmnopqrstuvwxyz'}
soma_pares = 0
existeImpar = False

for letra in alfabeto:
  if alfabeto[letra] % 2 != 0:
    soma_pares += alfabeto[letra] - 1
    existeImpar = True
  else: 
    soma_pares += alfabeto[letra]

if existeImpar: 
  print(soma_pares + 1)
else:
  print(soma_pares)
