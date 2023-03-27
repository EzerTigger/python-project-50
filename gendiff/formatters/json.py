from json import dumps


def get_json(data):
    return dumps(data, indent=4)
