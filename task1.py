class Date:

    def __init__(self, date: str):
        """
        Инициализация элементов класса Дата
        :param date:Дата в виде строки формата dd-mm-yyyy
        """
        self.date = date

    @staticmethod
    def leap_year(year: int) -> bool:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    is_leap_year = True
                else:
                    is_leap_year = False
            else:
                is_leap_year = True
        else:
            is_leap_year = False
        return is_leap_year

    @classmethod
    def int_date(cls, str_date: str) -> list:
        result = str_date.split('-')
        result = list(map(int, result))
        return result

    @staticmethod
    def is_date(list_date: list) -> bool:
        days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        if 1 < list_date[1] > 12:
            raise ValueError('Введены некорректные данные')
        if Date.leap_year(list_date[2]) and list_date[1] == 2 and list_date[0] <= 29:
            pass
        elif list_date[0] <= days_in_month[list_date[1]-1]:
            pass
        else:
            raise ValueError('Введены некорректные данные')
        return True


date1 = Date('07-08-2020')
print(date1.date)
print(Date.int_date(date1.date))
print(Date.is_date(Date.int_date(date1.date)))
