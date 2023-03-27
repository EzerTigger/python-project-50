from gendiff.parsing import parsing_files
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import get_json
from gendiff.diff_dict import get_diff_dict


def get_lower_case_bool(arr):
    for char in arr:
        if isinstance(char, dict):
            for key, value in char.items():
                if isinstance(value, (list, dict)):
                    get_lower_case_bool(value)
                else:
                    if value is True:
                        char[key] = 'true'
                    elif value is False:
                        char[key] = 'false'
                    elif value is None:
                        char[key] = 'null'
    return arr


def choose_format(data, formatter):
    if formatter == 'plain':
        return plain(data)
    elif formatter == 'json':
        return get_json(data)
    elif formatter == 'stylish':
        return stylish(data)


def get_extension(file_name):
    extension = ''
    for i in range(len(file_name)):
        if file_name[i] == '.':
            extension = file_name[i + 1:]
    return extension


def generate_diff(first_file, second_file, form='stylish'):
    first_ext = get_extension(first_file)
    second_ext = get_extension(second_file)
    file_1 = parsing_files(first_file, first_ext)
    file_2 = parsing_files(second_file, second_ext)
    return choose_format(get_lower_case_bool(get_diff_dict(file_1, file_2)), form)
