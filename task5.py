import os

def numeric_string(string: str) -> str:
    """Функция проверяет, чтобы входящая строка состояла только из чисел через пробелы.
    Любые не числовые 'слова' будут удалены
    """
    str_el_list = string.split()
    string = ' '
    i = 0  # счетчик списка из "слов" строки
    while i < len(str_el_list):
        if str_el_list[i].isdigit():
            i += 1
            continue
        else:
            try:
                if not float(str_el_list[i]):
                    str_el_list[i] = '0'
                i += 1
            except ValueError:
                str_el_list.pop(i)
    return string.join(str_el_list)


file_path = os.path.join(os.path.dirname(__file__), 'text_file5.txt')
try:
    os.remove(file_path)
except FileNotFoundError:
    pass
while True:
    user_input = input('Введите строку из чисел через пробел. Пустая строка - конец ввода\n')
    if not user_input:
        break
    else:
        string_of_numbers = numeric_string(user_input)
    with open(file_path, 'a', encoding='UTF-8') as working_file:
        working_file.write(f'{string_of_numbers} ')
