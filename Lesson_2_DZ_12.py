from random import randint
"""Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих 
чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
Ввод:
7
12
Вывод
3 4 или 4 3  """



sum_number = int(input("Введите сумму двух чисел  "))
product_of_number = int(input("Введите произведение двух чисел  "))

for i in range(sum_number):
    for j in range(product_of_number):
        if sum_number == i + j and product_of_number == i * j:
            print(f"Ваши числа {i}, {j}")
    


