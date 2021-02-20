import json

python_dict = {"name": "Pang", "age": 21, "city": "Chonburi"}

json_string = json.dumps(python_dict)

print(json_string)