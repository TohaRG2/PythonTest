import random

count_of_elements = 5
max_index = 0
maximum = 0
mas = [int(input()) for i in range(count_of_elements)]
# print(mas)
summa = 0
for i in range(count_of_elements):
    element = mas[i]
    print('число', element, '  ', 'номер числа', i)
    is_need2add = True
    last = element % 10
    element = element // 10     # можно закомментировать, но без нее непонятно
    while element > 0:
        if last != element % 10:
            is_need2add = False
        element = element // 10
    if is_need2add:
        summa += mas[i]
        print("Добавляем:", mas[i])

print()
print("Сумма чисел с одинаковыми цифрами:", summa)
