from itertools import product, permutations


def f(w, x, y, z):
    return (not (((not x) or y) and (not w))) or (not (z and (not (y and w))))


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(0, a1, a2, 1), (a3, 1, a4, a5), (1, 0, a6, a7)]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            u = [f(**(dict(zip(p, t)))) for t in table]
            if u == [0, 0, 0]:
                print(*p)


print(3840 * 2160)
print(65536 / 8294400)
print(8294400 * 16)