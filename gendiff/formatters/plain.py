def get_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value in ['true', 'false', 'null'] or type(value) == int:
        return value
    else:
        return f'\'{value}\''


def get_plain(value):
    def iter_(current_value, ancestry):
        lines = []
        for child in current_value:
            if child['type'] == 'add':
                action = f"added with value: {get_value(child['value'])}"
                ancestry.append(child['key'])
                name = ".".join(ancestry)
                lines.append(f"Property '{name}' was {action}")
                ancestry.pop()
            elif child['type'] == 'del':
                action = 'removed'
                ancestry.append(child['key'])
                name = ".".join(ancestry)
                lines.append(f"Property '{name}' was {action}")
                ancestry.pop()
            elif child['type'] == 'changed':
                action = f"updated. From {get_value(child['value1'])} to " \
                         f"{get_value(child['value2'])}"
                ancestry.append(child['key'])
                name = ".".join(ancestry)
                lines.append(f"Property '{name}' was {action}")
                ancestry.pop()
            elif child['type'] == 'root':
                ancestry.append(child['key'])
                lines.append(iter_(child['value'], ancestry))
                ancestry.pop()
        return '\n'.join(lines)

    return iter_(value, [])
