def my_len(array):
    """Принимает итерабельный элемент и считает его длину"""
    i = 0
    for _ in array:
        i += 1
    return i


def one_word_check(string: str) -> bool:
    """Принимает на вход строку и проверяет, чтобы в ней было
    только одно слово из букв английского алфавита
    """
    letters_code = [('A', 'Z'), ('a', 'z')]
    for letter in string:
        is_word = False
        for array in letters_code:
            if ord(letter) in range(ord(array[0]), ord(array[len(array) - 1]) + 1):
                is_word = True
                break
        if not is_word:
            return False
    return True


def one_word_lower(string: str) -> str:
    """Принимает на вход строку - одно слово, делает все буквы в слове маленькими и возвращает строку"""
    # Коды заглавных букв английского и русского алфавитов
    letters_code = ('A', 'Z')
    result_string = ''
    for letter in string:
        if ord(letter) in range(ord(letters_code[0]), ord(letters_code[1]) + 1):
            result_string = result_string + chr(ord(letter) + 32)
        else:
            result_string = result_string + letter
    return result_string


def one_word_title(string: str) -> str:
    """Принимает на вход строку - одно слово из строчных букв,
    делает первую букву в слове заглавной и возвращает строку"""
    result_string = ''
    i = 0
    for letter in string:
        if i == 0:
            result_string = result_string + chr(ord(letter) - 32)
        else:
            result_string = result_string + letter
        i += 1
    return result_string


user_string = input('Введите несколько слов из английских букв через пробел\n')
result = ''
final_result = ''
list_of_words = user_string.split()
all_words_ok = True
for word in list_of_words:
    if one_word_check(word):
        word = one_word_lower(word)
        word = one_word_title(word)
        result = result + word + ' '
    else:
        all_words_ok = False
j = 0
for symb in result:
    if j < my_len(result) - 1:
        final_result = final_result + symb
        j += 1
if all_words_ok:
    print(final_result)
else:
    print('ОШИБКА: Все слова в строке должны состоять только из английских букв')
