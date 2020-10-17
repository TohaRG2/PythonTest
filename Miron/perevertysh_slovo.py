st = "конституция"
n = len(st) - 1
newSt = ""
for i in range(n, -1, -1):
    newSt += st[i]
print(newSt)
