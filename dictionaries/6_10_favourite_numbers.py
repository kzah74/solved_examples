favourite_numbers = {
    'mike': [3, 5, 7],
    'kristyan': [5, 2, 8],
    'simon': [1, 6, 4],
    'rex': [8, 10, 52], 
    'federico': [10, 4, 80],
    }

for name, numbers in favourite_numbers.items():
    print(name.title() + "`s favourite numbers are: ")
    for number in numbers:
        print("- " + str(number))