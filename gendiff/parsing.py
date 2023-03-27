import json
import yaml


def parsing_files(file_name, file_ext):
    file = open(file_name)
    if file_ext in ['yaml', 'yml']:
        result_file = yaml.safe_load(file)
    elif file_ext == 'json':
        result_file = json.load(file)
    else:
        raise TypeError("Incorrect File Extension")
    return result_file
