import json

with open("File2.json", "r") as json_file:
    file_data = json.load(json_file)

print(file_data["address"][2]["street"])

New_data = {'country': 'Ukraine', 'region': 'Kharkivska', 'city': 'Kharkiv', 'street': 'Sumska', 'house': 9, 'flat': 11}

file_data["address"].append(New_data)

print(json.dumps(file_data, indent=3))

with open("File2.json", "w") as json_file:
    json.dump(file_data, json_file, indent=4)
