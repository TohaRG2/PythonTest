qq = int(input())
jojo = list(range(qq))
for i in range(qq):
    jojo[i] = int(input())

for i in range(qq // 2):
    jojo[i] = jojo[qq - 1 - i]

print(jojo)

