def describe_city(name, country='Italy'):
    """Describe a city with the name of a city and its country"""
    print(f"{name.title()} is in {country.title()}.")

describe_city('viareggio')
describe_city(name='pisa')
describe_city('new york', "United States of America")