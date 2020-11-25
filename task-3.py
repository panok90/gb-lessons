# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц(зима, весна, лето, осень).Напишите решения через list и через dict.
number_month = int(input("Введите номер месяца: "))
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
season = {'Зима': winter, 'Весна': spring, 'Лето': summer, 'Осень': autumn}
for key in season:
    if number_month in season[key]:
        print(key)
        break
