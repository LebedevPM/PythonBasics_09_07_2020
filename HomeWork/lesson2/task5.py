rating = [7, 5, 3, 3, 2]  # первоначальный рейтинг
user_rate_list = []  # список пользовательских значений
aux_var = 'last_symb'  # вспомогательная переменная для увеличения списка rating
# ввод пользовательских значений
while True:
    user_rate = input('Введите натуральное число. Если хотите закончить заполнение рейтинга, введите пусто значение.\n')
    if user_rate == '':
        break
    if user_rate.isdigit():
        user_rate = int(user_rate)
        user_rate_list.append(user_rate)
    else:
        print('Вы должны ввести натуральное число. Чтобы закончить заполнение рейтинга, введите пусто значение.\n')
print(rating)
for elem1 in user_rate_list:
    i = 0  # счетчик элементов в rating от начала до места вставки пользовательского значения
    j = len(rating)  # счетчик для прохода rating от конца до места вставки пользовательского значения
    for elem2 in rating:
        if elem1 > elem2:  # поиск первого элемента, меньше вставляемого, чтобы новый элемент был ПОСЛЕ таких же как он
            # list.insert нашел позже, не стал переписывать, т.к. по сути сам написал тоже самое
            rating.append(aux_var)
            while j != i:
                rating[j] = rating[j - 1]
                j -= 1
            rating[j] = elem1
            break
        i += 1
print(rating)
