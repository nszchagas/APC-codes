a, b = input().split(' ')

tamanho = len(b)
a_cortada = a[-len(b):]

if a[-len(b):] == b:
    print('ta dentro!!!')
else: 
    print('ta fora...')