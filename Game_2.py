# Добавляем проверку введенных чисел, взять можно 1, 2 или 3 камешка из кучи и не больше чем в куче всего камней

kucha = int(input("Введите начальное количество камней: "))
cheyHod = 2

while kucha > 0:
    if cheyHod == 1:
        cheyHod = 2
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
