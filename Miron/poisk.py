st = "с: main   second  third   forth    file.py  "

count = 0

position = st.rfind(" ")
while position == len(st) - 1:
    st = st[:len(st) - 1]
    position = st.rfind(" ")

position = st.find(" ")
while position == 0:
    st = st[1:]
    position = st.find(" ")

while position != -1:
    count += 1
    st = st[position + 1:]
    position = st.find(" ")
    while position == 0:
        st = st[1:]
        position = st.find(" ")

count += 1
print(count)
