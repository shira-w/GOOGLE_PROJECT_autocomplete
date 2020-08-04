import re
import linecache
import json

from auto_complete_data import AutoCompleteDataClass
from json.decoder import JSONDecodeError


def str_to_regular(str, i):
    str2 = str[:i] + '.' + str[i + 1:]
    return str2


def str_to_regular_2(str, i):
    str2 = str[:i] + '.' + str[i:]
    return str2


def change_to_auto_complete_data(c, prefix, sub_score):
    with open("files.json", "r") as f:
        try:
            files = json.load(f)
        except JSONDecodeError:
            pass
        str_sen = linecache.getline(files[c[0]], c[1])
        score = len(prefix) * 2 - sub_score
        return AutoCompleteDataClass(str_sen, files[c[0]], c[1], 1, score)


def get_best_k_completions(prefix):
    atoComp = []
    file_name = prefix[0] + ".json"
    with open(file_name, "r") as f:
        cache_of_user = json.load(f)
    cache_of_user_dict = cache_of_user[0]
    comp = cache_of_user_dict.get(prefix)

    if comp:
        for c in comp:
            atoComp.append(change_to_auto_complete_data(c, prefix, 0))
        if len(atoComp) == 5:
            return atoComp

    all_option = []
    for index in range(1, len(prefix)):  # o(n)
        comp = cache_of_user_dict.get(str_to_regular(prefix, index))
        if comp:
            for c in comp:  # o(1)
                if index >= 4:
                    all_option.append(change_to_auto_complete_data(c, prefix, 1))
                else:
                    all_option.append(change_to_auto_complete_data(c, prefix, 5 - index))
    all_option.sort(reverse=True, key=lambda w: w.score)
    atoComp = atoComp + all_option[:5 - len(atoComp)]

    if not atoComp:
        return None
    return atoComp

