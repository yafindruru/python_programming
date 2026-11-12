# Mengakses file json
import json

DATA_FILE_NAME = 'files/history_city_list.json'
with open(DATA_FILE_NAME, 'r', encoding='Latin1') as jsonfile:
    data = json.load(jsonfile)

print(type(data))
print(len(data))

# print(data[764])
print(json.dumps(data[764], indent=4))