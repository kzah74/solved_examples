people = []

person = {
    'first_name': 'andrea',
    'last_name': 'buratti',
    'age': 32,
    'city': 'sofia',
    'number_of_child': 1,
}
people.append(person)

person = {
    'first_name': 'andrew',
    'last_name': 'williams',
    'age': 31,
    'city': 'sofia',
    'number_of_child': 1,
}
people.append(person)    

person = {
    'first_name': 'mike',
    'last_name': 'baldi',
    'age': 27,
    'city': 'sofia',
    'number_of_child': 0,
}
people.append(person)

for person in people:
    full_name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    number_of_child = person['number_of_child']
    
    if number_of_child == 1:
        print(f"{full_name}, of {city}, is {age} years old and has "
        f"{number_of_child} child.")
    else:
        print(f"{full_name}, of {city}, is {age} years old and has "
        f"{number_of_child} children.")