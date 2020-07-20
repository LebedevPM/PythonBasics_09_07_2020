seasons = ['зиме', 'весне', 'лету', 'осени']
season_month_num = {
    'зиме': [1, 2, 12],
    'весне': [3, 4, 5],
    'лету': [6, 7, 8],
    'осени': [9, 10, 11]
}
# пользовательский ввод номера месяца
while True:
    user_month_num = input('Введите номер месяца\n')
    if user_month_num.isdigit():
        user_month_num = int(user_month_num)
        if 1 <= user_month_num <= 12:
            break
        elif user_month_num == 0:
            print('Нулевого месяца не существует')
            continue
        else:
            print('В году только 12 месяцев')
            continue
    else:
        print('Номер месяца - всегда натуральное число.\n')
# решение через список
if user_month_num < 3:
    user_season = seasons[0]
elif user_month_num < 6:
    user_season = seasons[1]
elif user_month_num < 9:
    user_season = seasons[2]
elif user_month_num < 12:
    user_season = seasons[3]
else:
    user_season = seasons[0]
print(f'Вы выбрали {user_month_num:>2} месяц, он относится к {user_season:>5}')
# решение через словарь
for key, value in season_month_num.items():
    if user_month_num in value:
        user_season = key
print(f'Вы выбрали {user_month_num:>2} месяц, он относится к {user_season:>5}')
