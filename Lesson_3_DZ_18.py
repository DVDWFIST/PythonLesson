from random import randint
"""Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n) 
самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5"""


n = int(input("Введите кол-во чисел в массиве:  "))
n_list = [randint(1, 10) for i in range(n)]
print(n_list)
k = int(input("Введите число для поиска ближайшего:  "))

b = [abs(k - i) for i in n_list]

print(f" Ближайшее к вашему числу {k} являеться число: {n_list[b.index(min(b))]} ")

