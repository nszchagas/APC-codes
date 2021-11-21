notas = [] 
entrada = float(input())

while entrada != -1: 
    notas.append(entrada)
    entrada = float(input())

def media(lista):
    media = 0
    for x in lista:
        media+= x
    return media/len(lista)
    

print(int(media(notas)))

    