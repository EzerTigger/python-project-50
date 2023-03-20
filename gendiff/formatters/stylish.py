import itertools


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
