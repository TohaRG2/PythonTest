st = input()
n = len(st) -1
j = ""
h = ""
for i in range(n,-1,-1):
    j = st[i]
    h += j
print(h,j)