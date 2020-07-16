"""Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

while True:
    user_num = input('Введите  целое положительное число отличное от 0 \n')
    if user_num.isdigit() and int(user_num) != 0:
        user_num = int(user_num)
        break
    else: print('Вы должны ввести целое положительное число отличное от 0')
max_num = 0
tmp = user_num
while tmp != 0:
    if max_num < tmp % 10:
        max_num = tmp % 10
    if max_num == 9:
        break
    tmp = tmp // 10
print('Вы ввели: ', user_num, ', максимальная цифра в этом числе: ', max_num)