cities = {
    'sofia': {
    'country': ' bulgaria',
    'population': '1 milion',
    'fact': 'Sofia is the capital of Bulgaria',
    },
    'milano': {
    'country': ' italia',
    'population': '2 milion',
    'fact': 'Milano is the fashion capital of Italy',
    },
    'new york': {
    'country': ' united states of America',
    'population': '8000000',
    'fact': 'New york is the best city of USA',
    },
}

for city, information in cities.items():
    print("\nFor " + city.title() + " we have the next information:")
    for key, value in information.items():
        print("\t- " + key + ": " + value.title())

for city, information in cities.items():
    country = information['country'].title()
    population = str(information['population'])
    fact = information['fact']

    print("\n" + city.title() + " is in " + country + ".")
    print("The population of the city is " + population + ".")
    print("Interesting fact about the city is that " + fact + ".")