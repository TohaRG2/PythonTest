# /Volumes/Data_Mac/Test
# S.strip([chars])	Удаление пробельных символов в начале и в конце строки
import re

from my_functions.files_def import *
from my_functions.string_def import *

directory = '/Volumes/Data_Mac/Test/src'
trg_directory = '/Volumes/Data_Mac/Test/trg'
in_file = '/Volumes/Data_Mac/Test/src.txt'
out_file = '/Volumes/Data_Mac/Test/trg/test.xml'
log_file = '/Volumes/Data_Mac/Test/log.txt'
recreate_dir(trg_directory)

lf = open(log_file, 'w')
files = os.listdir(directory)
for file in files:
    f = open(directory + "/" + file)
    out_f = open(trg_directory + "/" + file, 'w')
    for line in f:
        newline = line
        pattern = "(?<=(Алгоритм:</a>.))..*?(?=<)"
        alg = re.search(pattern, line)
        if alg:
            print(alg[0])
            p = re.compile(r'<.*?>')
            sub_str = p.sub('', alg[0]).strip().replace(" ", "_")
            newline = substring_before("\">Алгоритм", line) + '&alg=' + sub_str + substring_after("\">Алгоритм", line)
            lf.write(file + " - " + newline)
        out_f.write(newline)
    out_f.close()

lf.close()
# show_file(out_file)

# for file in files:
#     print(file)
