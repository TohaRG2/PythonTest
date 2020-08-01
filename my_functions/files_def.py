import shutil
import os


def show_file(filename):
    file = open(filename)
    for line in file:
        if line.endswith('\n'):
            newline = line[0:len(line) - 1]
        else:
            newline = line
        print(newline)


def recreate_dir(directory):
    try:
        shutil.rmtree(directory)
        os.makedirs(directory)
    except OSError as e:
        print("Ошибка: %s : %s" % (directory, e.strerror))
