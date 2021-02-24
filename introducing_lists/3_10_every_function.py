countries = ['bulgaria', 'italy', 'france', 'england', 'sweden']
print(countries[3].title())
message = f"My favourite countri is {countries[1].title()}."
print(message)
countries[3] = 'spain'
print(countries)
countries.append('england')
print(countries)
countries.insert(3, 'greece')
print(countries)
del countries[-1]
print(countries)
popped_country = countries.pop(3)
print(countries)
print(popped_country.title())
removed_country = 'sweden'
countries.remove(removed_country)
print(removed_country)
print(countries)
countries.remove('france')
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)
countries.sort()
print("\nHere is the sorted list:")
print(countries)
print(sorted(countries, reverse=True))
print(countries)
countries.reverse()
print(countries)
countries.reverse()
print(countries)
print(len(countries))


