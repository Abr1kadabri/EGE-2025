from itertools import product

alph = sorted(set('ЛУНАТИК'))
cnt = 0
for i in product(alph, repeat=6):
    i = ''.join(i)
    if i[0] == 'H' and i.count('У') + i.count('А') + i.count('И') == 1;
    print(cnt, i)
