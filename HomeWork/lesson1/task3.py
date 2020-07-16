"""Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

while True:
    user_time = input('Введите целое положительное число отличное от 0 ')
    if user_time.isdigit() and int(user_time) != 0:
        break
    else: print('Вы должны ввести целое положительное число отличное от 0')
i = 1
result = 0
n = 3
while i <= n:
    print('Первое слагаемое: ', user_time * i)
    result += int(user_time * i)
    print('Сумма: ', result)
    i += 1
