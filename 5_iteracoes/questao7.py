qtd = int(input())
peixe = input()

def mensagem(peixe, qtd):
    if peixe == "salmão":
        print(2*qtd*"Que salmão bonito que pesquei!\n")
    elif peixe == "atum":
        print(qtd*"Nossa, pesquei um atum gigante!\n")
    else:
        print("Nem sabia que esse peixe existia")

mensagem(peixe, qtd)
