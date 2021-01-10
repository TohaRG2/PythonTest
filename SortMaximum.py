mas = [0, 1, 2, 4, 5, 3, 6, 7, 10, 9, 15]
n = len(mas)
# for i in range(n):
#     mas[i] = int(input())

for i in range(n - 1):
    nMax = i
    for j in range(i + 1, n):
        if mas[j] > mas[nMax]:
            nMax = j
    if nMax != i:
        mas[i], mas[nMax] = mas[nMax], mas[i]

print(mas)
