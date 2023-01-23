from gendiff.parsing import parsing_files


def stringify(value):
    """Get dict and return it as string"""

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
    """Convert True and False to lowercase string"""

    lower = {True: 'true', False: 'false'}
    for k, v in dict_.items():
        if isinstance(v, dict):
            bool_to_lower_case(v)
        else:
            if v in lower:
                dict_[k] = lower[v]
    return dict_


def generate_diff(first_file, second_file):
    file_1, file_2 = parsing_files(first_file, second_file)
    result_dict = {}
    keys = sorted(set(list(file_1.keys()) + list(file_2.keys())))
    for key in keys:
        if key not in file_1:
            result_dict[f"  + {key}"] = file_2[key]
        elif key not in file_2:
            result_dict[f"  - {key}"] = file_1[key]
        elif file_1[key] != file_2[key]:
            result_dict[f"  - {key}"] = file_1[key]
            result_dict[f"  + {key}"] = file_2[key]
        else:
            result_dict[f"    {key}"] = file_1[key]
    return stringify(bool_to_lower_case(result_dict))


"""

Проблемы:
Валятся тесты
"""
# print(generate_diff('tests/fixtures/flat/file1.json', 'tests/fixtures/flat/file1.json'))
