favourite_places = {
    'mike': ['dubai', 'new york', 'shri lanka'],
    'andrea': ['sofia', 'argentina', 'bora bora'],
    'federico': ['new york', 'dominicana', 'cuba'],
}

for name, places in favourite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())