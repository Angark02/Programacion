# Default Arguments
def make_shirt(size="L", message="I Love Python"):
    """Display info about making the T-shirt"""
    print(f"Welcome to Bershka!\nThe size {size} T-shirt you ordered have been printed with the message:\n'{message.title()}'\n")
    
make_shirt()
make_shirt(size="M")
make_shirt(size="XS", message="I Love Videogames")