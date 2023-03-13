""" Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет
на круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта
система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном списке содержащим количество ягод на кустах.

Input: 2 2 1 3 2
Output: 7 """

garden_bed = list(map(int, input('Введите список: ').split()))

together = 3
max_bushes = sum(garden_bed[:together])
count = len(garden_bed)

for i in range(count):
    if i <= count - together:
        current_bushes = sum(garden_bed[i:i + together])
    else:
        current_bushes = (
            sum(garden_bed[:together - (count - i)]) +
            sum(garden_bed[i:]))
    if max_bushes < current_bushes:
        max_bushes = current_bushes

print(max_bushes)