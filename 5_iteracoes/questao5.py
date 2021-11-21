qtd = int(input())

entrada = int(input())

menor = entrada
maior = entrada

for x in range(qtd-1):
    entrada = int(input())
    if entrada > maior:
        maior = entrada
    if entrada < menor:
        menor = entrada

print(f"Menor: {menor} \nMaior: {maior}")

