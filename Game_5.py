# Добавляем немного реализма, компьютер будет иногда ошибаться, но не на последних ходах, когда в куче не меньше скольки
# камней (задается настройкой)

import random

# настроечные параметры
computerDoNotMistake = 5        # если в куче меньше, то компьютер не должен ошибаться
mistakePercent = 10             # процент, при котором компьютер будет выбирать случайный ответ, вместо правильного

# Основная программа
kucha = int(input("Введите начальное количество камней: "))
cheyHod = 2

while kucha > 0:
    print("Сейчас в куче", kucha, "камешков")
    if cheyHod == 1:
        cheyHod = 2
        kamni = kucha % 4
        if kamni == 0:
            kamni = random.randint(1, 3)
        else:
            isComputerRight = random.randint(1, 100)
            if isComputerRight < mistakePercent and kucha > computerDoNotMistake:
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
