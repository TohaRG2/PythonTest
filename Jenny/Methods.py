def print_some_var(value):
    digit = 5
    print(value)


def show_index(x, z):
    print(x)
    z = z * 2
    print(z)


def show_res(digit):
    global number
    q = digit * number
    print(q)


letter = input("Введите букву")
string = letter + " - это буква"
digit = int(input("Введите цифру"))
number = digit * 987

print_some_var(letter)

a = string.find(" ")
y = string.find("к")
show_index(a, y)

print_some_var(digit)
