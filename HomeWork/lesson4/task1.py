from sys import argv

_, work_hour, work_hour_price, bonus, *__ = argv

try:
    salary = float(work_hour) * float(work_hour_price) + float(bonus)
    print(salary)
except ValueError:
    print('Количество отработанных часов, ставка работника за один час и премия должны быть числами')
