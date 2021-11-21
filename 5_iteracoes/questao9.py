def isPrimo(num):
    if num >= 2:
        cont = 2
        while cont**2 <= num:
            if num % cont == 0: 
                return False
            cont+=1
        return True
    else: 
        return False

        
ano = int(input())
if isPrimo(ano):
    print("Emidio")
else: 
    print("Faina")
