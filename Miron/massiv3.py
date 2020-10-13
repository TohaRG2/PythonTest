# primer = input()
primer = "1+2+3+4"
chislo1 = ""
chislo2 = ""
intoger1 = 0
plus2 = primer.rfind("+")
poschis = primer[plus2:]
poschis = int(poschis)
otvet = 0
otvet += poschis
plus = primer.find("+")
while plus != -1:
    chislo1 = primer[:plus]
    print(chislo1)
    primer = primer[plus+1:]
    intoger1 = int(chislo1)
    otvet += intoger1
    plus = primer.find("+")
print(otvet)

primer = "1+2+3+4"
mas = primer.split("+")
summ = 0
for i in mas:
    summ += int(i)
print(summ)
