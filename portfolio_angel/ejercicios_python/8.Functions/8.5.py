# CIties
def describe_city(city, country="Spain"):
    """Display info about a city and where its located"""
    print(f"{city.title()} is in {country.title()}.")
    
describe_city("Málaga")
describe_city("Barcelona")
describe_city("London", "England")