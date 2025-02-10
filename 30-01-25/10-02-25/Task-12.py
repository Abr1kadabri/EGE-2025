# Нашлось
a1 = '24'
a2 = '1234'
print(a1 in a2)

# Заменить все вхождения
st = '123123411'
st = st.replace('1', '*')
print(st)

# Заменить один раз
st = '123123411'
st = st.replace('1', '*', 1)
print(st)

# Формирование строки определенной длины
st = '1' * 100
print(st)

# Сумма цифр числа
# Способ 1 
summ = 0
for i in st:
    summ += int(i)

# Способ 2
summ = sum(int(i) for i in st)

# Способ 3
summ = sum(map(int, st))



