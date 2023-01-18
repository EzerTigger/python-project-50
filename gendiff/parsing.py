import json
import yaml


def parsing_files(first_file, second_file):
    if first_file.endswith(('yml', 'yaml')):
        file_1 = yaml.safe_load(open(first_file))
        file_2 = yaml.safe_load(open(second_file))
    else:
        file_1 = json.load(open(first_file))
        file_2 = json.load(open(second_file))
    return file_1, file_2


# print(parsing_files('files/file1.json', 'files/file2.json'))
