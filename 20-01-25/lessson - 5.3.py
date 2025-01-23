num1 = 5
num2 - 30

f1 = num1 % 2 == 0
f2 = num2 % 10 == 0
f3 = 10 <= num1 + num2  <= 99

if f1 and f2:
    print('Text1')
if f1 or f2:
    print('Text2')
if not f1 and f2:
    print('Text3')
if (f2 == f3) and f1:
    print('Text4')