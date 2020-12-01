# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
string = input("Введите строку: ")
basic_list = list(string)
count_elements = len(basic_list)
last_element = None
if count_elements % 2:
    last_element = basic_list[count_elements - 1]
    basic_list.pop(count_elements - 1)
new_list = []
i = 0
while True:
    if i < count_elements - 1:
        new_list.append(basic_list[i + 1])
        new_list.append(basic_list[i])
        i += 2
    else:
        break
if count_elements % 2:
    new_list.append(last_element)
print(new_list)
