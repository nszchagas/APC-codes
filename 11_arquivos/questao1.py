def aprendendoArquivos(fileName):
  with open(fileName, 'r', encoding='utf-8') as file:
    firstLine = file.readline()
    if firstLine[-1] == '\n':
      firstLine = firstLine[:-1]
    try: 
      numero = int(firstLine)
      print('42 eh a resposta para tudo!')
    except ValueError:
      print(f'Ola {firstLine}!')
      
    
      