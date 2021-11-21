
TAXA = 0.025 

cotacao = float(input())
tamanho_lote = int(input())
qtd_lotes = int(input())

custo_lote = cotacao * tamanho_lote * (1 + TAXA)

for x in range(1,qtd_lotes+1):
    print(f"Lote: {x} - Total da venda: R$ {custo_lote:.2f}")