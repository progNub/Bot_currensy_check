import json

file_name_sum = "sum.json"


def read_json(file_name):
    try:
        with open(file_name, 'r') as f:
            print("read complite")
            return json.load(f)
    except IOError:
        print("read is not complete: " + file_name)
        return False


def write_to_json(file_name, data):
    try:
        with open(file_name, 'w+') as f:
            json.dump(data, f, indent=2)
            print("write complite")
    except IOError:
        print("write is not complete: " + file_name)


