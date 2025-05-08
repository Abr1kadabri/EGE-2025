from itertools import permutations

graph = 'HG GC CF FA AE EH HB BG BD DF DE'.split()
matrix = '367 568 18 58 247 127 156 234 '.split()
print(*range(1,9))
for i in permutations('ABCDEFGH'):
    res = []
    for x, y in graph:
        res.append(str(i.index(x) + 1) in matrix[i.index(y)])
    if all(res):
        print(*i)
