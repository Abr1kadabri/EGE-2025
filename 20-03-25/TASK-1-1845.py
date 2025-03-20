from itertools import permutations

graph = 'BA BG GE EZ ZD DV BA GD BV'.split() # ['BA', 'BG', 'GE'.....]
matrix = '67 567 456 35 234 123 12'.split()

print(*range(1,8))
for i in permutations('ABGEZVD'):
    res = []
    for x, y in graph:
        res.append(str(i.index(x) + 1) in matrix[i.index(y)])
    if all(res):
        print(*i)
