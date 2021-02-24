people = []

person = {
    'first_name': 'andrew',
    'last_name': 'williams',
    'age': 32,
    'city': 'sofia',
}
people.append(person)

person = {
    'first_name': 'kristyan',
    'last_name': 'ivanov',
    'age': 31,
    'city': 'sofia',
}
people.append(person)    

person = {
    'first_name': 'simon',
    'last_name': 'phillips',
    'age': 27,
    'city': 'sofia',
}
people.append(person)

for person in people:
    full_name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    
    print(f"{full_name}, of {city}, is {age} years old.")