palavra, qtdLinhas, filePath = input().strip().split(' ')
qtdLinhas = int(qtdLinhas)


with open(filePath, 'r', encoding='utf-8') as arquivo:
  texto = arquivo.readlines()

for i in range(len(texto)):
  if palavra in texto[i]:
    print(f'{filePath}: {i+1}')
    if i - qtdLinhas >= 0:
      begin = i - qtdLinhas
    else: 
      begin = 0
    if i + qtdLinhas <= len(texto) - 1:
      end = i + qtdLinhas
    else:
      end = len(texto) - 1
    for linha in texto[begin:end+1]:
      if linha[-1] != '\n':
        print(linha)
      else:
        print(linha, end='')
    print('')
  

