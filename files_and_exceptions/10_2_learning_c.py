filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.strip()
    print(line.replace('Python', 'C'))
print("\n")

# "strip()" can be in the print statement.
for line in lines:
    print(line.strip().replace('Python', 'C'))