import json

filename = 'favourite_number.json'
user_number = int(input("Tell me your favourite number: "))
with open(filename, 'w') as f:
    json.dump(user_number, f)
