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


def goldao(num):
    for b in range(num+1):
        if isPrimo(num) and isPrimo(b):
            return (b, num)
        else: 
            num -= 1
        

