def print_some_var(value):
    digit = 3
    print(value)
    print(digit)


def show_index(x, z):
    print(x)
    z = z * 2
    print(z)


def show_res(digit):
    global number
    q = digit * number
    print(q)


letter = "a"
string = letter + " - это буква"
digit = 5
number = digit * 9

print_some_var(letter)

a = string.find(" ")
y = string.find("к")
show_index(a, y)

print_some_var(digit)
