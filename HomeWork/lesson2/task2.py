var_list = []
i = 0
#заполнение списка с клавиатуры пока не будет введена пустая строка
while True:
    new_element = input('Вводите значения списка. Если захотите закончить ввод, введите пустое значение\n')
    if new_element == '':
        break
    var_list.append(new_element)
print(var_list)
if len(var_list) % 2 == 0:
    while i < len(var_list):
        if i % 2 != 0:
            aux_var = var_list[i-1]
            var_list[i-1] = var_list[i]
            var_list[i] = aux_var
        i += 1
else:
    while i < len(var_list) - 1:
        if i % 2 != 0:
            aux_var = var_list[i-1]
            var_list[i-1] = var_list[i]
            var_list[i] = aux_var
        i += 1
print(var_list)