# City Names
def city_country(city, country):
    """Display info about a city and where its located"""
    return f"{city.title()}, {country.title()}"

city = city_country("Málaga", "Spain")
print(city)

city = city_country("Barcelona", "Spain")
print(city)

city = city_country("London", "England")
print(city)