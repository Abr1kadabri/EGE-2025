from itertools import permutations

graph = 'CE EG GF FA AC CD DH HE FB BA'.split()
matrix = '68 47 45 237 368 15 248 157 '.split()

print(*range(1,9))
for i in permutations('ABCDEFGH'):
    res = []
    for x,  y in graph:
        res.append(str(i.index(x) + 1) in matrix[i.index(y)])
        print(*i)
