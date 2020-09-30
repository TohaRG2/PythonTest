import random

st = ""
for i in range(10):
    r = random.randint(0, 1)
    if r == 0:
        st += "X"
    else:
        st += "."
print(st)

newSt = ""
for i in range(len(st)):
    if st[i] == "X":
        newSt += "1"
    else:
        newSt += "0"

print(newSt)
