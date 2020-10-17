import random
import time
print(" Привет,добро пожаловать в игру ГЛАДИАТОР!")
print("ПРАВИЛА:")
print("1-Не использовать авто клик")
print("2-Не смотреть код")
print("3-Писать адекватные имена")
print("Привет,ты не мог бы представиться?")
playername=input()
print("Класное имя!",playername)
sword=random.randint(1,10)
print("Выберите меч")
swordnumb=int(input())
if swordnumb==1:
    print("Деревянный меч")
    print("Характеристики:")
    print("Урон:2")
    print("Вес:Ультра легкий")
if swordnumb==2:
    print("Оловянный меч")
    print("Характеристики:")
    print("Урон:4")
    print("Вес:Легкий")
if swordnumb==3:
    print("Железный меч")
    print("Характеристики:")
    print("Урон:6,5")
    print("Вес:Средний")
if swordnumb==4:
    print("Зачарованный меч")
    print("Характеристики:")
    print("Урон:8")
    print("Вес:Тяжелый")
if swordnumb==5:
    print("Меч небесного война")
    print("Характеристики:")
    print("Урон:9,3")
    print("Вес:Очень тяжелый")
if swordnumb==6:
    print("Клинок наемника")
    print("Характеристики:")
    print("Урон:8,4")
    print("Вес:Ультра легкий")
if swordnumb==7:
    print("Трезубец")
    print("Характеристики:")
    print("Урон:12")
    print("Вес:Ультра тяжелый")
if swordnumb==8:
    print("Боевой топор")
    print("Характеристики:")
    print("Урон:12")
    print("Вес:Тяжелый")
if swordnumb==9:
    print("Нож бабочка")
    print("Характеристики:")
    print("Урон:7")
    print("Вес:Ультра легкий")
if swordnumb==10:
    print("Катана")
    print("Характеристики:")
    print("Урон:16")
    print("Вес:Средний")
heath=5
glheath = 5
for i in range(1,5):
    print("Вот ты и на арене,какой ход ты сделаешь?(1-удар 2-защита")
    hit=int(input())
    if hit==2:
        print("Ты уклонился")
    else:
        print("Ты попал в Гладиатора")
        glheath = glheath - 1
        print("У него осталось", glheath, "жизней")
    print("Теперь ход противника")
    hit2=random.randint(1,2)
    if hit2==1:
        print("Противник промазал")
    else:
        print("Противник попал в тебя")
        heath-=1
        print("У тебя осталось",heath,"жизней")