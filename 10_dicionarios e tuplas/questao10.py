frase = input()

def contaLetras(palavra, categoria):
  
  qtd_vogais = 0
  palavraLower = palavra.lower()
  
  for l in palavraLower:
    if l in categoria.lower(): 
      qtd_vogais += 1

  return qtd_vogais

numeros = {
  'consoantes' : contaLetras(frase, 'bcdfghjklmnpqrstvwxyz'),
  'vogais' : contaLetras(frase, 'aeiou')
} 

print(numeros)
