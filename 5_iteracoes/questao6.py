def getPrimos(num):
    primos = []
    for numero in range(2,num+1):
        if isPrimo(numero):
            primos.append(numero)
    return primos


def isPrimo(num):
    cont = 2
    while cont**2 <= num:
        if num % cont == 0: 
            return False
        cont+=1
    return True


def contador_divisores(num):
    multiplicidades = []
    qtd_divisores = 1
    for fator_primo in getPrimos(num):
        if num % fator_primo == 0:
            quociente = num / fator_primo
            qtd = 1
            while quociente % fator_primo == 0:
                qtd+=1
                quociente = quociente / fator_primo
            multiplicidades.append(qtd)
    for x in multiplicidades: 
        qtd_divisores *= (x+1)
    return qtd_divisores

entrada = int(input())
menor_numero = entrada
qtd_divisores = 0


for x in range(1, entrada+1):
    divisores_x = contador_divisores(x)
    if divisores_x > qtd_divisores:
        menor_numero = x 
        qtd_divisores = divisores_x

print(f"{menor_numero} {qtd_divisores}")
