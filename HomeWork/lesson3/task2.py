def user_data(name, surname, birth_date, tel_num, email):
    """Функция принимает данные пользователя и выводит их на экран в строку"""

    return f'{surname.lower().title()} {name.lower().title()}, Дата рождения: {birth_date}, ' \
           f'Контактные данные: {tel_num}, {email.lower()} '


print(user_data(surname='пУпкИн', email='eXaMPLe@maIl.ru', name='вАсИЛий',
                tel_num='8 (123) 456-78-90', birth_date='01/02/1234'))
