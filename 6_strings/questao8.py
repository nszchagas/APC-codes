qtd_consultas = int(input())

for x in range(qtd_consultas):
  inicio, fim, texto = input().split(' ')
  inicio = int(inicio)
  fim = int(fim)
  string_cortada = texto[inicio:fim+1][::-1]
  print(string_cortada)