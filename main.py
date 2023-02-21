import os
from pprint import pprint

#Задача 1. Читаем книгу рецептов из файла.
file_w_path = os.path.join(os.getcwd(), 'recipes.txt')

with open(file_w_path, encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingr_count = int(file.readline())
        dish_ingr = []
        for _ in range(ingr_count):
            ingr_full =  file.readline().strip()
            ingr, qnt, meas = ingr_full.split(' | ')
            dish_ingr.append(
                {'ingridient' : ingr,
                'quantity' : qnt,
                'measure' : meas}
            )
        cook_book[dish_name] = dish_ingr
        file.readline()

#Проверяем, что книга рецептов в правильном формате
pprint(cook_book)

#Задача 2. Определяем функцию для формирования спика покупок
def get_shop_list_by_dishes(dishes, person_count):
    buy_list = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            if ingr['ingridient'] not in buy_list.keys():
                buy_list[ingr['ingridient']] = {
                    'measure' : ingr['measure'],
                    'quantity' : person_count * int(ingr['quantity'])
                }
            else:
                buy_list[ingr['ingridient']]['quantity'] = int(buy_list[ingr['ingridient']]['quantity']) + int(person_count * int(ingr['quantity']))
    return buy_list

#Проверяем, что функция выводит данные в заданном формате
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

#Задача 3. Объединяем файлы по условию из задания.
file_1 = '1.txt'
file_2 = '2.txt'
file_3 = '3.txt'
file_res = 'result.txt'

def count_lines(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        num_lines = len(file.readlines())
    return num_lines

dict = {file_1 : count_lines(file_1), file_2 : count_lines(file_2), file_3 : count_lines(file_3)}
dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}

with open(file_res, 'w', encoding='utf-8') as file:
    for x in dict.keys():
        with open(x, 'r', encoding='utf-8') as inner_file:
            file.write(x + '\n')
            file.write(str(count_lines(x)) + '\n')
            for line in inner_file:
                file.write(line.strip() + '\n')

#Открыв файл, убеждаемся, что формат соответствует заданному    

#Задание 4 выполнено.