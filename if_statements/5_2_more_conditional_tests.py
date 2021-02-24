my_food = 'soup'
if my_food == 'soup':
    print("Yes, it is true.")

if my_food != 'pizza':
    print("No, it is not true.")

if my_food != 'soup':
    print("No, it is not true.")
else:
    print("Yes, it is true.")
print("\n")

registred_person = 'mike'
if registred_person == 'mike':
    print("Mike can publish it.")
else:
    print("Mike can`t publish it.")

if registred_person == 'Mike'.lower():
    print("Mike can publish it.")
else:
    print("Mike can`t publish it.")


number = 23
if number == 23:
    print("\nTrue")
else:
    print("False")

if number != 41:
    print("True")
else:
    print("False")

if number >= 23:
    print("True")
else:
    print("False")

if number <= 23:
    print("True")
else:
    print("False")

if number < 25:
    print("True")
else:
    print("False")

if number > 21:
     print("True")
else:
    print("False")

if number > 25:
    print("True")
else:
    print("False")


cars = 'honda', 'bmw', 'audi'
if cars == 'honda' or 'kia':
    print("\nTrue")
else:
    print("False")

if cars == 'honda' and 'kia':
    print("True")
else:
    print("False")

if 'honda' in cars:
    print('\nYes, "Honda" is in the list.')

if 'kia' not in cars:
    print('\nNo, "Kia" is not in the list.')
