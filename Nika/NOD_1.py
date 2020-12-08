x = int(input())
y = int(input())

while x != 0 and y != 0:
    if x > y:
        x = x % y
    else:
        y = y % x
nod = x + y

print(nod)
