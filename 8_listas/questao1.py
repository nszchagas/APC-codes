qtd_meias = int(input().strip())
cores = input().split()
cores_diferentes = []
sozinhas = []
for cor in cores:
  if cor not in cores_diferentes:
    cores_diferentes.append(cor)

for cor in cores_diferentes:
  if cores.count(cor) % 2 != 0:
    sozinhas.append(cor)

if len(sozinhas) == 0:
  print("tudo certo")
else:
  print(f"{sozinhas[0]} sozinho")
