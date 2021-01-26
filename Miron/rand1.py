import random

count_of_elements = 20
max_index = 0
maximum = 0
mas = [random.randint(100, 999) for i in range(count_of_elements)]
print(mas)

for i in range(count_of_elements):
    print('число', mas[i], '  ', 'номер числа', i)
    summa = 0
    while mas[i] > 0:
        summa += mas[i] % 10
        mas[i] = mas[i] // 10
    print('сумма', summa)
    if summa > maximum:
        maximum = summa
        max_index = i

print("номер максимального числа: ", max_index, 'максимальное число: ', maximum)
