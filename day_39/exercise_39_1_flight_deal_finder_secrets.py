import json

def read_secrets():
    with open("day_39/secrets.json", "r") as file:
        data = json.load(file)
    return data



