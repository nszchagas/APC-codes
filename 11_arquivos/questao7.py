import os

filePath = input().strip().split(' ')[-1]

if os.path.isfile(filePath):
  print('O arquivo existe')
else: 
  print('Arquivo inexistente')