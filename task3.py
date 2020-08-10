class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


user_list = []
while True:
    user_input = input('Заполняйте список числами поэлементно (Элемент - Enter).\n'
                       'Если хотите закончить ввод, введите команду "stop"\n'
                       'Вводите: \n')
    if user_input.lower() == 'stop':
        break
    else:
        try:
            if is_digit(user_input):
                user_list.append(user_input)
            else:
                raise MyError('Просил же вводить ТОЛЬКО числа!!!')
            continue
        except MyError as err:
            print(err, user_input)
print(user_list)
