def get_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value in ['true', 'false', 'null'] or type(value) == int:
        return value
    else:
        return f'\'{value}\''


def get_plain(value):
    def iter_(current_value, path):
        lines = []
        for char in current_value:
            if char['type'] == 'add':
                action = f"added with value: {get_value(char['value'])}"
                path.append(char['key'])
                name = ".".join(path)
                lines.append(f"Property '{name}' was {action}")
                path.pop()
            elif char['type'] == 'del':
                action = 'removed'
                path.append(char['key'])
                name = ".".join(path)
                lines.append(f"Property '{name}' was {action}")
                path.pop()
            elif char['type'] == 'changed':
                action = f"updated. From {get_value(char['value1'])} to " \
                         f"{get_value(char['value2'])}"
                path.append(char['key'])
                name = ".".join(path)
                lines.append(f"Property '{name}' was {action}")
                path.pop()
            elif char['type'] == 'root':
                path.append(char['key'])
                lines.append(iter_(char['value'], path))
                path.pop()
        return '\n'.join(lines)

    return iter_(value, [])
