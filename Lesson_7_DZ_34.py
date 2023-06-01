s = input("Введите стихотворение: ").split()
vowels = []
for word in s:
    count = 0
    for letter in word:
        if letter in "aeiouAEIOU":
            count += 1
    vowels.append(count)
if len(set(vowels)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")