# Задача 1:
# Напишите программу, которая принимает на вход вещественное число
#  и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num_list = input('Введите вещественное число: ')
num_list = num_list.replace('.','') # Убираем точку из вещественного числа
# (и получаем список без точки)
def find_sum(list): # создаем функцию цикла для списка
    print(list)
    sum=0
    for i in range(len(list)): # пробегаем по всей длине списка
        sum += int(list[i]) # складываем индексы(преобразованные из строки в число)
    return sum
print(find_sum(num_list))
 