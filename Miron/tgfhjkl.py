s = input()
qq = ''
toto = ''
kol = 0
flag = True
while qq != -1 and toto != -1:
    qq = s[0]
    s = s[1:]
    kol = len(s) - 1
    toto = s[kol]
    s = s[:kol]
    if qq != toto:
        flag = False
        break
if flag == True:
    print('its perevyortysh')
else:
    print('its not perevyortysh')