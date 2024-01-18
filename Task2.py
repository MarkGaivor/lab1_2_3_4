import csv
import json


def converter(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        json_data = []
        for row in reader:
            data = {}
            for column, value in row.items():
                data[column] = value
            json_data.append(data)
    json_string = json.dumps(json_data, indent=4)
    return json_string

csv_file = 'data.csv'
json_string = converter(csv_file)
print(json_string)