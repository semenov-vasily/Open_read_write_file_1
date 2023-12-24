import os
from pprint import pprint


# Функция ч_1 задания. Создание словаря блюд
def cook_book_read():
    cook_book = {}
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read().split('\n\n')
        for dish in data:
            dish = dish.split('\n')
            ingrdns_all = []
            for ingr in dish[2:]:
                ingrdns = {}
                ingrdns['ingredient_name'], ingrdns['quantity'], ingrdns['measure'] = ingr.split('|')
                ingrdns['quantity'] = int(ingrdns['quantity'])
                ingrdns_all.append(ingrdns)
            cook_book[dish[0]] = ingrdns_all
    return cook_book


cook_book = cook_book_read()
print(cook_book)


# Функция ч_2 задания. Создание словаря ингредиентов
def get_shop_list_by_dishes(dishes, person_count):
    ingrs_list = {}
    for dish_name in dishes:
        for ingr in cook_book[dish_name]:
            dict_ingrs = {}
            if ingr['ingredient_name'] not in ingrs_list:
                dict_ingrs['measure'] = ingr['measure']
                dict_ingrs['quantity'] = ingr['quantity'] * person_count
                ingrs_list[ingr['ingredient_name']] = dict_ingrs
            else:
                ingrs_list[ingr['ingredient_name']]['quantity'] = ingrs_list[ingr['ingredient_name']]['quantity'] + \
                                                                  ingr['quantity'] * person_count
    return ingrs_list


pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель', 'Омлет'], 2))


# Функция ч_3 задания. Создание списка файлов
def list_file_create(txt):
    dict_file = {}
    list_file = os.listdir("txt")
    print(list_file)
    for i in list_file:
        with open(txt + '\\' + i, 'r', encoding='utf-8') as f:
            file_1 = f.readlines()
            dict_file[i] = len(file_1)
    return dict_file


list_file_create('txt')


# Запись в файл
def file_res(txt):
    list_tuple = list(list_file_create(txt).items())
    print(list_tuple)
    list_sorted = [i[0] for i in sorted(list_tuple, key=lambda items: items[1])]
    os.remove('write_file.txt')
    for name_file in list_sorted:
        with open('write_file.txt', 'a', encoding='utf-8') as f_1:
            with open(txt + '\\' + name_file, 'r', encoding='utf-8') as f:
                text_file = f.readlines()
            f_1.write(name_file + '\n')
            f_1.write(str(len(text_file)) + '\n')
            f_1.writelines(text_file)
            f_1.write('\n')
    return


file_res('txt')
