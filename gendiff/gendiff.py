import json
import argparse


# file1 = json.load(open('files/file1.json'))
#  file2 = json.load(open('files/file2.json'))


def parse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args


def stringify(value):

    def foo(current_value):
        result = "{\n"
        if type(current_value) == dict:
            for e in current_value:
                if type(current_value[e]) == dict:
                    result += f"{e}: {foo(current_value[e])}\n"
                else:
                    result += f'{e}: {current_value[e]}\n'
        else:
            return str(current_value)
        return result + '}'

    return foo(value)


def bool_to_lower_case(dict_):
    lower = {True: 'true', False: 'false'}
    for k, v in dict_.items():
        if v in lower:
            dict_[k] = lower[v]
    return dict_


def generate_diff(first_file, second_file):
    file_1 = json.load(open(first_file))
    file_2 = json.load(open(second_file))
    result_dict = {}
    keys = sorted(set(list(file_1.keys()) + list(file_2.keys())))
    for key in keys:
        if key not in file_1:
            result_dict[f" + {key}"] = file_2[key]
        elif key not in file_2:
            result_dict[f" - {key}"] = file_1[key]
        elif file_1[key] != file_2[key]:
            result_dict[f" - {key}"] = file_1[key]
            result_dict[f" + {key}"] = file_2[key]
        else:
            result_dict[f"   {key}"] = file_1[key]
    return stringify(bool_to_lower_case(result_dict))


"""
Скрипт работает. 
Теперь нужно, чтобы пакет работал как библиотека.
Проблемы:

"""
# print(generate_diff('files/file1.json', 'files/file2.json'))
