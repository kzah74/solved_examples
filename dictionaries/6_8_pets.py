pets = []

pet = {
    'kind': 'dog',
    'owner': 'mike',
    'name': 'tommy'
}
pets.append(pet)

pet = {
    'kind': 'cat',
    'owner': 'vanya',
    'name': 'pitt' 
}

pets.append(pet)

for pet in pets:
    print(f"The animal is {pet['kind']} with name {pet['name'].title()} and "
        f"owner {pet['owner'].title()}.")

for pet in pets:
    print("\nThis is what we know:")
    for key, value in pet.items():
        print("- " + key + ": " + value)