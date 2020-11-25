# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер
# товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
goods = []
an_list = []
number = 1
while number < 4:
    name = input(f"ТОВАР {number}. Название: ")
    price = int(input(f"ТОВАР {number}. Цена: "))
    count = int(input(f"ТОВАР {number}. Количество: "))
    unit = input(f"ТОВАР {number}. Еденица измерения: ")
    product = {"название": name, "цена": price, "количество": count, "eд": unit}
    an_list.append(product)
    good = (number, product)
    goods.append(good)
    number += 1
print(goods)
an_name = []
an_price = []
an_count = []
an_unit = []
for item in an_list:
    an_name.append(item["название"])
    an_price.append(item["цена"])
    an_count.append(item["количество"])
    if item["eд"] in an_unit:
        continue
    else:
        an_unit.append(item["eд"])
an_goods = {"название": an_name, "цена": an_price, "количество": an_count, "eд": an_unit}
print(f"Аналитика: {an_goods}")