def my_round(number: float, ndigits=0):
    """Округление числа до n знаков"""
    number = number * 10 ** ndigits // 1 / 10 ** ndigits
    return number


def div(a: float, b: float) -> float:
    """Функция деления двух чисел, учитывющая 0 в делителе. Округляет результат до двух знаков после запятой"""
    try:
        return my_round(a / b, 2)
    except ZeroDivisionError:
        print('Делитель не может быть равен нулю\n')


while True:
    dividend = input('Введите делимое\n')
    divider = input('Введите делитель\n')
    try:
        dividend = float(dividend)
        divider = float(divider)
        break
    except ValueError:
        print('Делимое и делитель должны быть числами\n')
print(div(dividend, divider))
