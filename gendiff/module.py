import json


file1 = json.load(open('files/file1.json'))
file2 = json.load(open('files/file2.json'))


def generate_diff(file_1, file_2):
    result_dict = {}
    keys = set(list(file_1.keys()) + list(file_2.keys()))
    for key in keys:
        if key not in file_1:
            result_dict[f"+ {key}"] = file_2[key]
        elif key not in file_2:
            result_dict[f"- {key}"] = file_1[key]
        elif file_1[key] != file_2[key]:
            result_dict[f"- {key}"] = file_1[key]
            result_dict[f"+ {key}"] = file_2[key]
        else:
            result_dict[key] = file_1[key]
    return json.dumps(result_dict)


print(generate_diff(file1, file2))