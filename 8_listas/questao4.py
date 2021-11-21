
from typing import no_type_check_decorator


dimensao = int(input())

vetor_u = list(map(int, input().strip().split(' ')))
vetor_v = list(map(int, input().strip().split(' ')))
produto_ortogonal = 0

for i in range(dimensao):
  produto_ortogonal += vetor_u[i]*vetor_v[i]

if produto_ortogonal == 0:
  print('ortogonais')
else:
  print(produto_ortogonal)