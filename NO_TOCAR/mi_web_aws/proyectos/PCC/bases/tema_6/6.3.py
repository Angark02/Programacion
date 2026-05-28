# Glossary / modelling an actual dictionary (we call it glossary to avoid confusion)
glossary = {
    "VPC": "Nube Privada Virtual",
    "IP": "Protocolo de Internet",
    "VM": "Virtual Machine",
    "S3": "Almacenamiento de objetos",
    "EC2": "Máquina Virtual de AWS",
}

for key, value in glossary.items(): # Realmente es un poco de trampa por que todavía no hemos visto bucles en diccionarios jejeje
    print (f"\n{key}:\n{value}") # Al añadir \n delante de {key} nos aseguramos de que se añada una línea en blanco antes de cada key-value.

# Usar este bucle viene muy bien cuando se usa en diccionarios cuyas keys guardan el mismo tipo de información (x ej.: el de las lenguas)
