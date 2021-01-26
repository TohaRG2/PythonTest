def coding(string, shift):
    result = ""
    for ch in string:
        result += chr(ord(ch) + shift)
    return result


st = input("Введите слово:")
sdvig = int(input("Введите сдвиг:"))
new_st = coding(st, sdvig)
print(new_st)
