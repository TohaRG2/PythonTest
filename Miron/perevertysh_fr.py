st = "Rfpfr rfpfr rfpfr"
isPolyndrom = True
st = st.replace(" ","")
st = st.lower()
n = len(st) - 1
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