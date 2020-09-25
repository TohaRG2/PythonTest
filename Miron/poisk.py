st = "c:/main/second/third/forth/file.py"

position = st.find("/")
while position != -1:
    print(st[:position])
    st = st[position+1:]
    position = st.find("/")
print(st)



