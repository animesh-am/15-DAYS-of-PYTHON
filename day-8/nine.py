import json

with open('nine.json', 'r') as file:
    data = json.load(file)

    print(data['name'])
