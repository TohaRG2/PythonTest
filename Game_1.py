# Основа для игры

kucha = int(input("Введите начальное количество камней: "))
cheyHod = 2

while kucha > 0:
    if cheyHod == 1:
        cheyHod = 2
    else:
        cheyHod = 1

    print("Сейчас в куче", kucha, "камешков")
    prompt = "Ходит игрок " + str(cheyHod) + " : "
    kamni = int(input(prompt))
    kucha -= kamni

print()
print("Выиграл игрок", cheyHod, "!!!")
