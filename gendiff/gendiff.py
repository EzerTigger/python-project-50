import itertools

from gendiff.parsing import parsing_files


def stylish(value, replacer=' ', spaces_count=4):
    def iter_(current_value, depth):

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        if not isinstance(current_value, list):
            if isinstance(current_value, dict):
                for k, v in current_value.items():

                    lines.append(
                        deep_indent + f"{k}: {iter_(v, deep_indent_size)}")
                result = itertools.chain("{", lines, [current_indent + "}"])
                return '\n'.join(result)
            else:
                return current_value

        for char in current_value:
            if char['type'] == 'add':
                new_deep = deep_indent[:-2]
                action = '+ '
                lines.append(
                    f'{new_deep}{action}{char["key"]}: '
                    f'{iter_(char["value"], deep_indent_size)}')
            elif char['type'] == 'del':
                new_deep = deep_indent[:-2]
                action = '- '
                lines.append(
                    f'{new_deep}{action}{char["key"]}: '
                    f'{iter_(char["value"], deep_indent_size)}')
            elif char['type'] == 'no_changed':
                new_deep = deep_indent
                action = ''
                lines.append(
                    f'{new_deep}{action}{char["key"]}: '
                    f'{iter_(char["value"], deep_indent_size)}')
            elif char['type'] == 'changed':
                new_deep = deep_indent[:-2]
                action = '- '
                lines.append(
                    f'{new_deep}{action}{char["key"]}: '
                    f'{iter_(char["value1"], deep_indent_size)}')
                new_deep = deep_indent[:-2]
                action = '+ '
                lines.append(
                    f'{new_deep}{action}{char["key"]}: '
                    f'{iter_(char["value2"], deep_indent_size)}')

            elif char['type'] == 'root':
                new_deep = deep_indent
                action = ''
                lines.append(
                    f'{new_deep}{action}{char["key"]}: '
                    f'{iter_(char["value"], deep_indent_size)}')

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)


def bool_to_lower_case(arr):
    """Convert True and False to lowercase string"""

    lower = {True: 'true', False: 'false', None: 'null'}
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
