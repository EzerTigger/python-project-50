from gendiff.parsing import parsing_files
from gendiff.formatters.stylish import stylish


def bool_to_lower_case(arr):
    """Convert True and False to lowercase string"""

    lower = {True: 'true', False: 0, None: 'null'}
    for char in arr:
        if isinstance(char, dict):
            for k, v in char.items():
                if isinstance(v, (list, dict)):
                    bool_to_lower_case(v)
                else:
                    if v in lower:
                        char[k] = lower[v]
    return arr


def generate_diff(first_file, second_file, form=stylish):
    file_1, file_2 = parsing_files(first_file, second_file)

    def diff_dict(dict1, dict2):
        result = []
        keys = sorted(set(list(dict1.keys()) + list(dict2.keys())))
        for key in keys:
            if key not in dict2:
                result.append({'type': 'del', 'key': key, 'value': dict1[key]})
            elif key in dict1 and key in dict2:
                if isinstance(dict1[key], dict) and isinstance(dict2[key],
                                                               dict):
                    result.append({'type': 'root', 'key': key, 'value': diff_dict(
                        dict1[key], dict2[key])})
                else:
                    if dict1[key] == dict2[key]:
                        result.append(
                            {'type': 'no_changed', 'key': key,
                             'value': dict1[key]})
                    else:
                        result.append({'type': 'changed', 'key': key,
                                       'value1': dict1[key],
                                       'value2': dict2[key]})

            else:
                result.append({'type': 'add', 'key': key, 'value': dict2[key]})
        return result

    return form(bool_to_lower_case(diff_dict(file_1, file_2)))
