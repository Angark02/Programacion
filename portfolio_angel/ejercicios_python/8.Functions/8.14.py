def make_car(manufacturer, model, **car_info): # Nos crea un diccionario llamado "car_info"
    """It stores information about a car in a dictionary"""
    car_info["manufacturer"] = manufacturer # Agregamos estos dos argumentos al diccionario
    car_info["model"] = model
    return car_info

car_profile = make_car("renault", "clio", # Agregamos el resto de argumentos que queramos
                       color="grey",
                       automatic=False)

print(car_profile)
