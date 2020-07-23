def my_round(number: float, ndigits=0):
    """Округление числа до n знаков"""
    number = number * 10 ** ndigits // 1 / 10 ** ndigits
    return number


def negative_raising(x: float, y: int) -> float:
    """Функция возведения числа в отрицательную степень

    :param x: float
    :param y: float
    :return: float
    """
    y = y * - 1
    result = 1
    # возведение в степень через умножение
    i = 0
    while i < y:
        result = result * x
        i += 1
    result = my_round(1 / result, 4)
    return result


while True:
    number = input('Введите действительсное положительное число X\n')
    degree = input('Введите целое отрицательное число Y\n')
    try:
        number = float(number)
        degree = int(float(degree))
        if number <= 0:
            print('X должен быть действительным положительным числом\n')
            continue
        elif degree >= 0:
            print('Y должен быть целым отрицательным числом\n')
            continue
        else:
            break
    except ValueError:
        print('X должен быть действительным положительным числом, а Y - целым отрицательным числом!\n')
print(f'{number} в степени {degree} равно {negative_raising(number, degree)}')
