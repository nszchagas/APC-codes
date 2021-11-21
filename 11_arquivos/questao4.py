with open('filmes.txt', 'r', encoding='utf-8') as filmes:
  content = filmes.readlines()

#A Origem/ação/250/n

filmes = dict()
GENERO, DURACAO = 0, 1

for filme in content:
  dados = filme.replace('\n', '').split('/')
  filmes[dados[0]] = [dados[1], int(dados[2])]

generoDesejado, tempoMax = input(), int(input())

def filter(): 
  filmesDisponiveis = []
  for opcao in filmes: 
    if filmes[opcao][GENERO].lower() == generoDesejado.lower() and filmes[opcao][DURACAO] <= tempoMax: 
      filmesDisponiveis.append(opcao)
  return filmesDisponiveis

sugestoes = filter()

if len(sugestoes) > 0:
  for filme in sugestoes:
    print(filme)
else: 
  print('Não foram encontrados filmes assim')
