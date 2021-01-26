def coding(string, shift):
    result = ""
    for ch in string:
        result += chr(ord(ch) + shift)
    return result


st = input("Введите слово:")
sdvig = int(input("Введите сдвиг:"))
print(coding(st, sdvig))
