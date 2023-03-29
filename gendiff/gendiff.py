from gendiff.parsing import parsing_files
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json
from gendiff.diff_dict import get_diff_dict


def get_lower_case_bool(tree):
    for node in tree:
        if isinstance(node, dict):
            for key, value in node.items():
                if isinstance(value, (list, dict)):
                    get_lower_case_bool(value)
                else:
                    if value is True:
                        node[key] = 'true'
                    elif value is False:
                        node[key] = 'false'
                    elif value is None:
                        node[key] = 'null'
    return tree


def choose_format(data, formatter):
    if formatter == 'plain':
        return get_plain(data)
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
