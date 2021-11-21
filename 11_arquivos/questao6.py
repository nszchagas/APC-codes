def palavras_repetidas(filePath, palavra):
  qtdVezes = 0
  with open(filePath, 'r', encoding='utf-8') as arquivo:
    for line in arquivo:
      qtdVezes += line.count(palavra)
  print(f'{palavra} aparece no arquivo {filePath} {qtdVezes} vez(es).')


