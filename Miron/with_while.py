s = input()
sNew = ""
i = 0
while i < len(s):
    c = s[i]
    if c == "p":
        c = "b"
    sNew += c
    i += 1
print(sNew)
