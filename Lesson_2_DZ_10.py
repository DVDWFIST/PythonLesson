from random import randint

"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, которые нужно 
перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть"""

n = int(input("Введите кол-во монет: "))
n_list = []
count = 0
two_count = 0
for i in range(n):
    n_list.append(randint(0, 1))

    if n_list[i] == 0:
        count += 1
    
    else:
        two_count += 1

print(n_list)

if count < two_count:
        print (f"Решек перевернуть: {count}")
    
else:
        print (f"Орлов перевернуть: {two_count}")
