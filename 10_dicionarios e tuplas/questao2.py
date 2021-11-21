qtd_cartazes, mudancas_direcao = map(int, input().split(' '))
cartazes = list(map(int, input().split(' ')))

inicio = cartazes[0]
cartazes.sort()

posicoes = {i : cartazes[i] for i in range(len(cartazes)) }



