import numpy as np


def include_substring(path_1: str, path_2: str):
    counter = 0
    with open(path_1, 'r', encoding='utf-8') as file_1:
        new_arr_1 = np.array(list(file_1.read()))
        string_arr_1 = ''.join(new_arr_1)
        splitted_arr_1 = string_arr_1.split(". ")
    with open(path_2, 'r', encoding='utf-8') as file_2:
        new_arr_2 = np.array(list(file_2.read()))
        string_arr_2 = ''.join(new_arr_2)
        splitted_arr_2 = string_arr_2.split(". ")

    for i in splitted_arr_1:
        for j in splitted_arr_2:
            if i == j:
                counter += 1
    print("Количество идентичных предложений в двух текстовых файлах:", counter)
    return counter


include_substring("/Users/southrussian/PycharmProjects/Laboratories/text_1.txt",
                  "/Users/southrussian/PycharmProjects/Laboratories/text_2.txt")
