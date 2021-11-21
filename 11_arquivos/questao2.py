f1, f2 = input().strip().split(' ')

with open(f1, 'r', encoding='utf-8') as file1, open(f2, 'r', encoding='utf-8') as file2: 
  content1, content2 = file1.read(), file2.read()
  if len(content1) == 1:
    print(f'O arquivo {f1} esta quase vazio, mas o {f2} nao esta!\n{content2}')
  elif len(content2) == 1:
    print(f'O arquivo {f2} esta quase vazio, mas o {f1} nao esta!\n{content1}')

  

