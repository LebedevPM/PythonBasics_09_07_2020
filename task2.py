class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    user_dividend = input('Введите делимое\n')
    user_divider = input('Введите делитель\n')
    try:
        user_dividend = float(user_dividend)
        user_divider = float(user_divider)
        if user_divider == 0:
            raise MyError('Делить на 0 не хорошо')
        quotient = user_dividend / user_divider
        print(quotient)
        break
    except ValueError:
        print('Вы должны вводить числа')
    except MyError as err:
        print(err)
