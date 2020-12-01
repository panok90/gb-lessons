# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
my_list = [7, 5, 3, 3, 2]
while True:
    value = input("Введите число или q чтобы закончить: ")
    if value == 'q':
        print(my_list)
        break
    value = int(value)
    max_value = my_list[0]
    min_value = my_list[-1]
    if value in my_list:
        first_index_value = my_list.index(value)
        count_value = my_list.count(value)
        position = first_index_value + count_value
        my_list.insert(position, value)
    elif value > max_value:
        my_list.insert(0, value)
    elif value < min_value:
        my_list.append(value)
    else:
        i = 0
        while i < len(my_list):
            if my_list[i] < value > my_list[i + 1]:
                my_list.insert(i, value)
                break
            i += 1
    print(my_list)
