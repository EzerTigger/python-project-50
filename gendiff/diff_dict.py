def get_diff_dict(dict1, dict2):
    result = []
    keys = sorted(set(list(dict1.keys()) + list(dict2.keys())))
    for key in keys:
        if key not in dict2:
            result.append({'type': 'del', 'key': key, 'value': dict1[key]})
        elif key in dict1 and key in dict2:
            if isinstance(dict1[key], dict) and isinstance(dict2[key],
                                                           dict):
                result.append({'type': 'root', 'key': key, 'value': get_diff_dict(
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
