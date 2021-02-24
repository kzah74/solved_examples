prompt = "Please, tell me your name: "
response = input(prompt)

filename = 'guest.txt'

with open(filename, 'a') as file_object:
    file_object.write(response)
