x = int(input())
#Оператор if работает с логическим условием.
# Если это условие истинно (True), то выполняется блок кода записанный внутри блока if.
# Если условие ложно, то блок внутри if пропускается и выполнение кода переходит
# на следующую после блока if строчку кода.

if x > 0:
    print('+')
#Чтобы добавить инструкции, которые будут выполняться в случае ложного выражения в условии,
# можно использовать оператор else.

elif x < 0:
    print('-')
    
#Чтобы добавить инструкции, которые будут выполняться в случае
# ложного выражения в условии, можно использовать оператор else.
else:
    print('0')

# Логические операции
# >, <, >=, <=, ==, !=
# not - меняет True на False, и наоборот

num1 = 10
print (not num1)

# and - возвращает True, только тогда, когда все значения True
num2 = 10
print (num2 > 0 and num2 % 3 == 0)

# or - возвращает True, когда хотя бы одно значение True
num3 = 20
print(num3 < 0 or num3 % 2 ==0)


num4 = 52
f1 = num4 % 2 == 0 #True
f2 = num4 == 100 #False
f3 = 10 <= num4 <= 99 #True

if f1 and f2 and f3: # True and False and True -> False
    print('Text2')
if f1 or f2 or f3: # True or False or True -> True
    print('Text1')
if f1 and f2 or f3: # True and False or True -> True
    print('Text3')
if f1 or f2 and f3:  # True or False and True -> True
    print('Text4')
if (f1 or f2) and f3 or f1 == f3 or f2:
    # (True or False) and True or True == True or False -> True
    print('Text5')
