import os


file_path = os.path.join(os.path.dirname(__file__), "text_file3.txt")
with open(file_path, 'r', encoding='UTF-8') as reading_file:
    sum_salary = 0
    employees_count = 0
    for line in reading_file:
        try:
            salary = int(line.split()[len(line.split()) - 1])
            if salary < 20000:
                print(line.split()[0])
            sum_salary += salary
            employees_count += 1
        except ValueError:
            print('В одной из строк файла зарплата не является числом')
    print(f'Средняя зарплата среди всех сотрудников составляет {sum_salary/employees_count}')
