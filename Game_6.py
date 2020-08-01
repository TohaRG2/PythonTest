# Переделаем на более сложную разновидность "камешков", из кучи можно брать степени двойки, т.е. 1,2,4,8,16 и т.д.

import random


def max_stepen2(chislo):
    stepen = 1
    while 2 ** stepen <= chislo:
        stepen += 1
    stepen -= 1
    return stepen


def chislo_podhodit(chislo):
    stepen = 0
    result = False
    while 2 ** stepen <= chislo:
        if 2 ** stepen == chislo:
            result = True
        stepen += 1
    return result


# настроечные параметры
computer_do_not_mistake = 5  # если в куче меньше, то компьютер не должен ошибаться
mistake_percent = 10  # процент, при котором компьютер будет выбирать случайный ответ, вместо правильного

# Основная программа
kucha = int(input("Введите начальное количество камней: "))
chey_hod = 2

while kucha > 0:
    print("Сейчас в куче", kucha, "камешков")
    if chey_hod == 1:
        chey_hod = 2
        sluch_stepen = random.randint(1, max_stepen2(kucha))
        kamni = 2 ** sluch_stepen
        is_computer_right = random.randint(1, 100)
        if is_computer_right > mistake_percent or kucha < computer_do_not_mistake:
            if kucha % 3 == 1:
                kamni = 2 ** (sluch_stepen - (sluch_stepen % 2))
            elif kucha % 3 == 2:
                kamni = 2 ** (sluch_stepen - ((sluch_stepen + 1) % 2))
        print("Компьютер взял", kamni)
    else:
        chey_hod = 1
        prompt = "Ходит игрок " + str(chey_hod) + " : "

        while True:
            kamni = int(input(prompt))
            if chislo_podhodit(kamni) and kamni <= kucha:
                break
            else:
                prompt = "Количество должно быть степенью двойки : "

    kucha -= kamni

print()
print("Игрок", chey_hod, "выиграл!!! Поздравляем!")
