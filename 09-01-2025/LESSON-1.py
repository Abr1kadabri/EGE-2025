var_float = 5.5
print (type(var_float))
var_int = 10
var_str = 'Privet'
var_list = [4, 6, 7, 'Privet', 6.9]
#Приведение типов данных необходимо для преобразования
# одного типа в другой, чтобы пояивалось возможность
# выполнять действия с нужным типом


# Преобразования типов осуществляется за счет вызова функции
# название которой совпадает с называнием типа данных


# Пример 1 (нельзя суммировать числа и строки. Поэтому мы превращаем строку в число
# при помощи команды int()):
num_1 = 100
str_1 = ('200')
print(num_1  + int(str_1))

# Пример 2 (Нельзя приписать число к строке. Поэтому мы превращаем число в строку
# при помощи команды str()):
welcom_text = 'Hello world'
id = 1
print(welcom_text + str(id))
