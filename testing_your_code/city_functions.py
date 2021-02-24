def get_city_country(city, country, population=''):
    """Generate a neatly formatted city_country name."""
    if population:
        city_country_name = f"{city.title()}, {country.title()}"
        city_country_name += f" - population {population}"
    else:
        city_country_name = f"{city.title()}, {country.title()}"
    return city_country_name