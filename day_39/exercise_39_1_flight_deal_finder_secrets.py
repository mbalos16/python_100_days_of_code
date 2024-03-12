import json

def read_secrets(secret):
    with open("day_39/secrets.json", "r") as file:
        data = json.load(file)
        secret = data.get(secret)
    return secret




