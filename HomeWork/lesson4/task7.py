def factorial(n: int):
    """Функция вычисляет факториал полученного на вход натурального числа n"""
    result = 1
    for el in range(1, n + 1):
        result *= el
        yield result


num = 15
print(factorial(num))
for idx, itm in enumerate(factorial(num), 1):
    print(idx, itm)
