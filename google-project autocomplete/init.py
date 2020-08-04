import json
import os
from os import walk
from os.path import join
import string
import re

from json.decoder import JSONDecodeError
from auto_complete_data import AutoCompleteDataClass


def from_key_to_regulars(key):
    regulars = []
    for index, k in enumerate(key):
        if 0 < index < len(key) - 1:
            regulars.append(key[:index] + '.' + key[index + 1:])
            regulars.append(key[:index] + key[index + 1:])
        if 0 < index < len(key):
            regulars.append(key[:index] + '.' + key[index:])

    regulars.append(key + ".")
    return regulars


def sub_strings(line):
    sub_str = []
    line = re.sub(' +', ' ', line)
    line = "".join(re.split("[^a-zA-Z0-9 ]*", line))
    line = line.casefold()
    len_ = len(line)
    for i in range(0, len_):
        if line[i - 1] == " " or i == 0:
            for j in range(i + 1, min(len_, i + 10)):
                sub_str.append(line[i:j])
                sub_str.extend(from_key_to_regulars(line[i:j]))

    return sub_str


def read_from_file(file):
    index_file = len(files) - 1
    # ==============================================
    print("FILE", file)
    # ==============================================
    for index_line, line in enumerate(file):
        if line.strip():
            substring = sub_strings(line)
            # ==================================
            print(substring)
            # ==================================

            for x in substring:
                data = [index_file, index_line + 1]
                json_name = x[0] + ".json"
                cache = [{}]
                if os.path.exists(json_name):
                    with open(json_name, "r")as f:
                        cache = json.load(f)

                if not cache[0].get(x):
                    cache[0][x] = []

                if len(cache[0][x]) < 5:
                    cache[0][x].append(data)

                with open(json_name, "w") as f:
                    json.dump(cache, f)  # what is indent 4?"""


files = []


def read_root(root_name):
    for root_name, dirs, files_name in os.walk(root_name):
        for index, file in enumerate(files_name):
            with open(os.path.join(root_name, file), "r", encoding='utf8') as auto:
                files.append(auto.name)
                with open("files.json", "w") as ff:
                    json.dump(files, ff)
                read_from_file(auto)

    print("==============end of init=================")


read_root("technology_texts")




