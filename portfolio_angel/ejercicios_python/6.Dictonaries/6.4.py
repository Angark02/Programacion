# Glossary 2
glossary = {
    "VPC": "Nube Privada Virtual",
    "IP": "Protocolo de Internet",
    "VM": "Virtual Machine",
    "S3": "Almacenamiento de objetos",
    "EC2": "Máquina Virtual de AWS",
}

for key, value in glossary.items(): 
    print (f"\n{key}:\n{value}") 

# Añadiendo nuevas key-pair
glossary["Ethernet"] = "Internet por cable"
glossary["Conmutador"] = "Nos permite conectar nodos"

for key, value in glossary.items():
    print (f"\n{key}:\n{value}") 