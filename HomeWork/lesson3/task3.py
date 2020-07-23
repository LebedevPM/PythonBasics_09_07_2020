def my_max(*args: float) -> float:
    """Функция нахождения максимума из переданных float элементов"""
    max_arg = args[0]
    for elem in args:
        max_arg = elem if elem > max_arg else max_arg
    return max_arg


def my_func(a: float, b: float, c: float) -> float:
    """Функция принимает три аргумента и возвращает сумму двух наибольших"""
    return my_max(a + b, a + c, b + c)


while True:
    num1 = input('Введите первое число')
    num2 = input('Введите втророе число')
    num3 = input('Введите третье число')
    try:
        num1 = float(num1)
        num2 = float(num2)
        num3 = float(num3)
        break
    except ValueError:
        print('Вы должны вводить числа')
print(my_func(num1, num2, num3))
