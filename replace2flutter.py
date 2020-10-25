# /Volumes/Data_Mac/Test
# S.strip([chars])	Удаление пробельных символов в начале и в конце строки
import re

from my_functions.files_def import *
from my_functions.string_def import *


def my_replace(some_file):
    new_file = some_file.replace(".xml", ".dart")
    i = new_file.find("_")
    if i > -1:
        new_file = new_file[:i] + new_file[i+1:].capitalize()
    out_f = open(trg_directory + "/" + new_file, 'w')
    # Добавляем хедер
    out_f.write(header_replace(header, new_file))
    with open(directory + "/" + some_file, "r") as in_f:
        in_f.readline()
        in_f.readline()
        for line in in_f:
            # обработка описаний массивов
            new_line = line.replace("<string-array name=\"", "static const ")
            new_line = new_line.replace("<integer-array name=\"", "static const ")
            if new_line.find("static const") > 0 and new_line.rfind("\">") > 0:
                new_line = new_line.replace("\">", " = [")
            new_line = new_line.replace("</integer-array>", "];")
            new_line = new_line.replace("</string-array>", "];")
            if new_line.find("<item>@string/") > 0:
                new_line = new_line.replace("</item>", ",")
            else:
                new_line = new_line.replace("</item>", "\",")
            new_line = new_line.replace("<item>@drawable/", "\"")
            new_line = new_line.replace("<item>@string/", "")
            new_line = new_line.replace("<item>", "\"")
            # Обработка описаний переменных для массивов
            new_line = new_line.replace("<string name=\"", "static const ")
            new_line = new_line.replace("\" formatted=\"false\"><![CDATA[", " = \"\"\"")
            if new_line.find("static const") > 0 and new_line.rfind("\">") > 0:
                new_line = new_line.replace("\">", " = \"")
            new_line = new_line.replace("]]></string>", "\"\"\";")
            new_line = new_line.replace("</string>", "\";")
            # Убираем лишнюю строчку в конце
            new_line = new_line.replace("</resources>", "}")

            out_f.write(new_line)

    out_f.close()


directory = '/Volumes/Data_Mac/TestFL/src'
trg_directory = '/Volumes/Data_Mac/TestFL/trg'
in_file = '/Volumes/Data_Mac/TestFL/src.txt'
out_file = '/Volumes/Data_Mac/TestFL/trg/test.xml'
log_file = '/Volumes/Data_Mac/TestFL/log.txt'
recreate_dir(trg_directory)
header = """
import 'package:rg2_flutter_getx/models/phases.dart';

class ClassName implements Phase {
  @override
  int count = phaseName_title.length;

  @override
  String phase = "PHASE_NAME";

  @override
  List<String> titles() => phaseName_title;

  @override
  List<String> icons() => phaseName_icon;

  @override
  List<String> descriptions() => phaseName_descr;

  @override
  List<String> urls() => phaseName_url;

  @override
  List<String> comments() => List.filled(count, "");

///==================================================

"""

lf = open(log_file, 'w')
files = os.listdir(directory)
for file in files:
    my_replace(file)
lf.close()
