st = "казак"
n = len(st) - 1
isPolyndrom = True
for i in range(len(st)//2):
    s1 = st[i]
    slast = st[n - i]
    if s1 != slast:
        isPolyndrom = False
        break
if isPolyndrom:
    print("перевертыш")
else:
    print("не перевертыш")