import json

def parse_json(file):
    with open(file) as in_f:
        data = json.load(f)
    return data