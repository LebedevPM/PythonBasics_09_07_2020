import os


def count_words_in_str(string: str) -> int:
    """Считает количество слов через пробел в строке.
    Учитываются пробелы в начале или в конце строки, а также множественные пробелы
    """

    word_flag = False  # флаг в слове мы или нет
    symbol_num = 0  # счетчик символов в строке
    word_num = 0  # счетчик слов в строке
    while symbol_num < len(string):
        if not word_flag and string[symbol_num] != ' ' and string[symbol_num].isalpha():
            word_num += 1
            word_flag = True
        elif word_flag and string[symbol_num] == ' ':
            word_flag = False
        symbol_num += 1
    return word_num


path_file = os.path.join(os.path.dirname(__file__), 'text_file2.txt')

with open(path_file, 'r', encoding='UTF-8') as reading_file:
    lines_count = len(reading_file.readlines())
    print(lines_count)
    reading_file.seek(0)
    for idx, line in enumerate(reading_file.readlines()):
        words_count = count_words_in_str(line)
        print(f'Строка {idx + 1:>2} - {words_count:>2} слов')
