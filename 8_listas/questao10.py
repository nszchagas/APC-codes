tam1, tam2 = map(int, input().split(' '))
tamanhoMax = max(tam1, tam2)
num1, num2= [0]*tamanhoMax, [0]*tamanhoMax

num1[:tam1] = map(int, input().split(' '))
num2[:tam2] = map(int, input().split(' '))


def soma(num1, num2):
  resultado = [0]*tamanhoMax
  for x in reversed(range(tamanhoMax)):
    soma = num1[x] + num2[x] + resultado[x]
    if soma > 1:  
      if x-1 >= 0: 
        resultado[x-1] += 1
      resultado[x] = soma - 2 
    else: 
      resultado[x] = soma
  return resultado


def formataBinario(binario):
  if len(binario) > 1:
    posicao = len(binario)-1
    ultimoUm = 0
    formatado = binario

    while formatado[posicao] == 0:
      posicao -= 1
    
    ultimoUm = posicao
    return formatado[:ultimoUm+1]
  else:
    return binario
    
   

for x in formataBinario(soma(num1, num2)):
  print(x, end=' ')


    
  
