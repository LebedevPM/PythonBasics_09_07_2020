dict_template = {
    'Наименование товара': ('Введите наименование товара', 'строка', str),
    'Цена товара': ('Введите цену товара', 'число', float),
    'Количество товара': ('Введите количество товара', 'целое число', int),
    'Единица измерения товара': ('Введите единицу измерения товара', 'строка', str),
}
product_list = []
product_num = 1
new_product = 'Да'
while new_product.title() == 'Да':
    product = {}
    for key, value in dict_template.items():
        while True:
            user_input = input(f'{value[0]}\n')
            try:
                user_input = value[2](user_input)
            except ValueError as err:
                print(f'{err}, {key} - всегда {value[1]}')
                continue
            product[key] = user_input
            break
    product_list.append((product_num, product))
    product_num += 1
    while True:
        new_product = input('Хотите ввести еще товар? Да или Нет')
        if new_product.title() == 'Да' or new_product.title() == 'Нет':
            break
        else:
            print('Введите Да или Нет')
print(product_list, '\n')
# собираем словарь аналитики
products_analitycs = {}
for key in dict_template:
    key_analitycs = []
    for value in product_list:
        key_analitycs.append(value[1][key])
    products_analitycs[key] = key_analitycs
print(products_analitycs)
