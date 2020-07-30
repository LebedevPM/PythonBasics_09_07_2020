import os

file_path = os.path.join(os.path.dirname(__file__), 'text_file4.txt')
new_file_path = os.path.join(os.path.dirname(__file__), 'text_file4_new.txt')
numbers = {
    1: 'Один',
    2: 'Два',
    3: 'Три',
    4: 'Четыре'
}
with open(file_path, 'r', encoding='UTF-8') as reading_file:
    first_line_flag = True  # флаг первой строки
    for line in reading_file:
        if line:  # только для не пустых строк, последняя строка исходного файла обязательно должна быть пустой
            try:
                num = int(line[-2])  # послений символ строки \n поэтому -2
            except ValueError:
                print('Нарушен формат записи в исходном файле')
                continue
            if num in numbers.keys():
                # Как открывать файл: если первая строка - 'w', чтобы создать или очистить  файл, если нет - 'a'
                if first_line_flag:
                    open_type = 'w'
                    first_line_flag = False
                else:
                    open_type = 'a'
                with open(new_file_path, open_type, encoding='UTF-8') as new_file:
                    new_file.write(f'{numbers[num]} - {num}\n')
            else:
                print('Исходный файл содержит неизвестное значение. Обновите словарь!')
