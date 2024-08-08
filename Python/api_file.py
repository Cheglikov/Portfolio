import os
import requests
import json

print(os.path.basename("C:\\Users\\Admin\\PycharmProjects\\pythonProject4\\api_file.py")[:-3].title())

response = requests.get('https://clients-rest.zdorovi.ua/api/user-goods?ids=2885&region=kv&townId=1240&lang=ua')

result = response.json()
print(json.dumps(result, indent=3))

print(result[0]["id"])
print(result[0]["menu"][3])
print(result[0]["priceRange"][-1])

with open("Execute_json.json", "w") as json_file:
    json.dump(result, json_file, indent=4)
