import os

file_path = os.path.join(os.path.dirname(__file__), 'text_file1.txt')
print(file_path)

with open(file_path, 'w', encoding='UTF-8') as text_f:
    while True:
        user_input = input('Введите текст\n')
        if user_input:
            text_f.write(f'{user_input}\n')
        else:
            break
