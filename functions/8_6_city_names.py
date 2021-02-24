def city_country(city, country):
    """Return a string for city and country"""
    information = (f"{city.title()}, {country.title()}")
    return information

variable = city_country('santiago', 'chile')
print(variable)

variable = city_country('new york', 'United States of America')
print(variable)

variable = city_country('milano', 'italy')
print(variable)