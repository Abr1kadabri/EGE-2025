from itertools import permutations

graph = 'AC CD DH HE EG GF FB BA CE FA'.split()
matrix = '68 47 45 237 368 15 248 157'.split()

print(*range(1, 8)) # Количество столбцов в матрице
for i in permutations('ABCDEFGH'):
   if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
       print(*i)
