"""Поработайте с переменными, создайте несколько, выведите на экран, запросите
у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

var_int = 10 # переменная с целым числом
var_float = 10.12345 # переменная с числом с плавающей точкой
var_str = 'ten' # переменная со строкой
var_multistr = """строковое
значение
из множества
строк"""
var_bool = True # переменная булиевая

# можно выводить переменные по одной
print(var_int)
print(var_float)
print(var_str)
print(var_multistr)
print(var_bool)

#можно вывести сразу много переменных
print(var_int, var_float, var_str, var_multistr, var_bool)

# тип переменной может поменяться если присвоить ей данные другого типа
var_tmp = var_int # вспомагательная переменная для смены типов
var_int = var_float
var_float = var_str
var_str = var_bool
var_bool = var_tmp
print(var_int, var_float, var_str, var_bool)

# данные для ввода можно запрашивать у пользователя
var_user = input('Введите целое число') # input - всегда строка
var_user = float(var_user) # на случай если введено дробное число
var_user = int(var_user)
print(var_user)

var_user = input('Введите число с дробной частью')
var_user = float(var_user)
print(var_user)

var_user = input('Введите текст')
print(var_user)

#bool от input - всегда True, если input заполнен (из-за того что строка). bool выдаст False только от False (не строка) или от числового 0.
var_user = input('Введите "булиевое" значение')
var_user = bool(var_user)
print(var_user)
var_user = input('Введите число 0')
var_user = int(var_user)
var_user = bool(var_user)
print(var_user)
