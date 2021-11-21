sequencia = list(map(int, input().strip().split(' ')))

inversoes = 0

for x in sequencia: 
  for i in range(sequencia.index(x), len(sequencia)):
    if x > sequencia[i]:
      inversoes += 1

print(inversoes)