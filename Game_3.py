# Сделаем подсказку только второму игроку, сколько камней нужно взять, чтобы выиграть.
# Используем random, когда нам все равно сколько камней взять

import random

kucha = int(input("Введите начальное количество камней: "))
cheyHod = 2

while kucha > 0:
    if cheyHod == 1:
        cheyHod = 2
        ostatok = kucha % 4
        if ostatok == 0:
            print("Похоже мы проигрываем, бери", random.randint(1, 3))
        else:
            print("Чтобы выиграть, нужно взять", ostatok, "камня")
    else:
        cheyHod = 1

    print("Сейчас в куче", kucha, "камешков")
    prompt = "Ходит игрок " + str(cheyHod) + " : "

    while True:
        kamni = int(input(prompt))
        if 1 <= kamni <= 3 and kamni <= kucha:
            break
        else:
            prompt = "Количество должно быть равно 1, 2 или 3 : "

    kucha -= kamni

print()
print("Игрок", cheyHod, "выиграл!!! Поздравляем!")
