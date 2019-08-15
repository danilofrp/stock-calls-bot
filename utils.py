import json


def read_json(file):
    with open(file, 'r') as f:
        json_str = f.read()
        data = json.loads(json_str)
    return data

    
def write_json(file, data):
    with open(file, 'w') as f:
        json_str = json.dumps(data)
        f.write(json_str)