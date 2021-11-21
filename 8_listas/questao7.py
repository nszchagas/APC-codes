posicao_termo = int(input())

chamadas_funcao = [0]*(posicao_termo+1)

def fibonacci(n):
  global chamadas_funcao
  chamadas_funcao[n] += 1

  if n == 0: 
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print(f'Termo: {fibonacci(posicao_termo)}')
print('Quantidades:')
for i in range(len(chamadas_funcao)):
  print(f'fibonacci({i}) - {chamadas_funcao[i]}')

