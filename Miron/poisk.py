st = "    ркенгшщлд неглшо  "

count = 0

position = st.rfind(" ")
while position == len(st) - 1:
    st = st[:len(st) - 1]
    position = st.rfind(" ")

position = st.find(" ")
while position == 0:
    st = st[1:]
    position = st.find(" ")

st = st.strip()

mas = st.split(" ")

while position != -1:
    count += 1
    st = st[position + 1:]
    position = st.find(" ")
    while position == 0:
        st = st[1:]
        position = st.find(" ")

count += 1
print(count)
print(len(mas))