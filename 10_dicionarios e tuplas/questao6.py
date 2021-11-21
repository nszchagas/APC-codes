CARACTERES = tuple('abcdefghijklmnopqrstuvwxyz0123456789')
dicionario_chars = dict()

texto = input().strip()

for char in CARACTERES: 
  dicionario_chars[char] = texto.count(char)

for char in dicionario_chars: 
  print(f'O caractere {char} aparece {dicionario_chars[char]} vez(es) na cadeia lida pelo programa :)')



