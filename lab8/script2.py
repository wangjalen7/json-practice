import json

file_path = '/workspace/json-practice/data/schacon.repos.json'

with open(file_path, 'r') as file:
    data = json.load(file)

csv_file_path = '/workspace/json-practice/lab8/chacon.csv'
with open(csv_file_path, 'w') as csv_file:
    for entry in data[:5]:
        csv_file.write(f"{entry['name']},{entry['html_url']},{entry['updated_at']},{entry['visibility']}\n")

csv_file_path
