lista = input().strip().split(' ')


def existeRepetido(lista):
  lista_unica = []
  for x in lista:
    if x not in lista_unica:
      lista_unica.append(x)
  for x in lista_unica:
    if lista.count(x) > 1:
      return True
  return False

print(existeRepetido(lista))


