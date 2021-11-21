n = int(input())

def mensagem(n):
    if n == 0:
        print("Ué? Já acabou?")
    elif n % 2 == 0:
        print("Bom dia!")
    else: 
        print("Boa noite!")

while n >= 0:
    mensagem(n)
    n -= 1