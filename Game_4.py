# Вместо второго игрока будет ходить компьютер, пока он всегда придерживается выигрышной стратегии

import random

kucha = int(input("Введите начальное количество камней: "))
cheyHod = 2

while kucha > 0:
    print("Сейчас в куче", kucha, "камешков")
    if cheyHod == 1:
        cheyHod = 2
        kamni = kucha % 4
        if kamni == 0:
            kamni = random.randint(1, 3)
        print("Компьютер взял", kamni, "камня")
    else:
        cheyHod = 1
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
