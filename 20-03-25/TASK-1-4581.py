from itertools import permutations

graph = 'AD DE EG GC CF FA EB AB BF'.split()
matrix = '37 367 125 56 34 247 126'.split()

print(*range(1,8))
for i in permutations('ABCDEFG'):
    res = []
    for x, y in graph:
        res.append(str(i.index(x) + 1) in matrix[i.index(y)])
    if all(res):
        print(*i)
