# Positional / Keywords Arguments
def make_shirt(size, message):
    """Display info about making the T-shirt"""
    print(f"Welcome to Bershka!\nThe size {size} T-shirt you ordered have been printed with the message:\n'{message.title()}'\n")
    
make_shirt("M", "Hello World!!")
make_shirt(message="GoodBye World!!", size="XS")