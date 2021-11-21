total_problemas = int(input())

qtd_certezas = 0
QTD_AMIGOS = 3
QTD_MIN_CERTEZAS = 2

for n in range(total_problemas):
    temp = 0
    certezas_n = input().split(' ')
    for i in range(QTD_AMIGOS):
        temp += int(certezas_n[i])
    if temp >= QTD_MIN_CERTEZAS:
        qtd_certezas += 1

print(qtd_certezas)