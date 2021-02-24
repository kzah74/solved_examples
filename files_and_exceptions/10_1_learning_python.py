filename = 'learning_python.txt'

with open (filename) as file_object:
    text = file_object.read()
    print(text + "\n")

with open (filename) as file_object:
    for line in file_object:
        print(line.strip())
print("\n")

with open (filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.strip())

