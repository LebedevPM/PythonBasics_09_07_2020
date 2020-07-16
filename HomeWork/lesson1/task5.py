"""Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

while True:
    revenue = input('Введите выручку фирмы\n')
    if revenue.isdigit():
        revenue = float(revenue)
        break
    else: print('Выручка - всегда положительное число.\n')
while True:
    costs = input('Введите издержки фирмы\n')
    if costs.isdigit():
        costs = float(costs)
        break
    else: print('Издержки - всегда положительное число.\n')
if revenue > costs:
    profit = revenue - costs
    profitability = profit / revenue * 100
    print('Отличный результат! Компания показала прибыль! Рентабельность составила ', profitability, '%')
    while True:
        count_of_employees = input('Введите количество сотрудников фирмы\n')
        if count_of_employees.isdigit():
            count_of_employees = int(count_of_employees)
            break
        else:
            print('Количество сотрудников - всегда целое положительное число.\n')
    profit_per_employee = profit / count_of_employees
    print('В расчете на одного сотрудника прибыль составила ', profit_per_employee, ' у.е. на человека')
elif revenue == costs:
    print('Выйти в ноль по итогам отченого периода - хороший результат в наше неспокойное время')
else:
    print('Сожалею, но Ваша компания показала убытки')
