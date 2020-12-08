n = int(input())
cub = 3 ** n
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(cub, fact)
