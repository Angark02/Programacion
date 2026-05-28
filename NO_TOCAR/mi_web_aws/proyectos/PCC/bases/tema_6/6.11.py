# Cities
cities = {
    "málaga": {
        "country": "spain",
        "population": "2 million",
    },
    
    "london": {
        "country": "england",
        "population": "5 million",
    },
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"\tCountry: {city_info["country"].title()}")
    print(f"\tPopulation: {city_info["population"].title()}")
    