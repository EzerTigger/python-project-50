import itertools

from gendiff.parsing import parsing_files


def stylish(value, replacer=' ', spaces_count=4):
    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            if key[0] == '+':
                new_deep = deep_indent[:-2]
                action = '+ '
                new_key = key[2:]
            elif key[0] == '-':
                new_deep = deep_indent[:-2]
                action = '- '
                new_key = key[2:]
            else:
                new_deep = deep_indent
                action = ''
                new_key = key
            lines.append(f'{new_deep}{action}{new_key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)


def bool_to_lower_case(dict_):
    """Convert True and False to lowercase string"""

    lower = {True: 'true', False: 'false', None: 'null'}
    for k, v in dict_.items():
        if isinstance(v, dict):
            bool_to_lower_case(v)
        else:
            if v in lower:
                dict_[k] = lower[v]
    return dict_


def generate_diff(first_file, second_file):
    file_1, file_2 = parsing_files(first_file, second_file)

    def diff_dict(dict1, dict2):
        result = {}
        keys = sorted(set(list(dict1.keys()) + list(dict2.keys())))
        for key in keys:
            if key not in dict2:
                result[f'- {key}'] = dict1[key]
            elif key in dict1 and key in dict2:
                if dict1[key] == dict2[key]:
                    result[f'{key}'] = dict1[key]
                else:
                    if isinstance(dict1[key], dict) and isinstance(dict2[key],
                                                                   dict):
                        result[key] = diff_dict(dict1[key], dict2[key])
                    else:
                        result[f'- {key}'] = dict1[key]
                        result[f'+ {key}'] = dict2[key]

            else:
                result[f'+ {key}'] = dict2[key]
        return result

    return stylish(bool_to_lower_case(diff_dict(file_1, file_2)))
# В таком виде выдаёт нужный результат. Теперь нужно разбить на
# создание дифа и представление, но не сломать.
