biblioteca = dict()
QTD_LIVROS = 5

for x in range(QTD_LIVROS):
  livro = input()
  qtd_livro = int(input())
  biblioteca[livro] = int(qtd_livro)

livro_buscado = input()

if livro_buscado in biblioteca.keys():
  print(f'Achei! Temos {biblioteca[livro_buscado]} exemplar(es)!')
else: 
  print('Poxa, não temos esse livro')
