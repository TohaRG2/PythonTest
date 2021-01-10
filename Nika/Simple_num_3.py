m = int(input())
n = int(input())
printed = True
for i in range(m, n + 1):
    simple = True
    for j in range(2, i):
        if i % j == 0:
            simple = False
            break
    if simple:
        print(i)
        printed = False
if printed:
    print(-1)
