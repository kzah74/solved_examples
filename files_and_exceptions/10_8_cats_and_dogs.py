filenames = ['cats.txt', 'dogs.txt']

def read_files(filenames):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"The file '{filename}' is missing.")
    else:
        print(f"The contents of the file '{filename}' is: \n{contents}\n")

for filename in filenames:
    read_files(filename)

