from itertools import permutations

graph = 'AB BC CF FG GE EA AD DA DF CD DB'.split()
matrix = '23567 145 146 23 127 137 156'.split()
print(*range(1, 8))
for i in permutations('ABCDEFG'):
    res = []
    for x, y in graph:
        res.append(str(i.index(x) + 1) in matrix[i.index(y)])
    if all(res):
        print(*i)