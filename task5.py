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
# удаляем файл, если такой уже есть
try:
    os.remove(file_path)
except FileNotFoundError:
    pass
# пользователь заполняет файл строками чисел
while True:
    user_input = input('Введите строку из чисел через пробел. Пустая строка - конец ввода\n')
    if not user_input:
        break
    else:
        string_of_numbers = numeric_string(user_input)
    with open(file_path, 'a', encoding='UTF-8') as working_file:
        working_file.write(f'{string_of_numbers}\n')
# считаем сумму чисел в файле
in_file_sum = 0
with open(file_path, 'r', encoding='UTF-8') as working_file:
    for line in working_file:
        list_from_line = line.split()
        j = 0
        while j < len(list_from_line):
            in_file_sum += float(list_from_line[j])
            j += 1
print(in_file_sum)
