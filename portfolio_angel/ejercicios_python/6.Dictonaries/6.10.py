# Favorite Numbers
favorite_numbers = {"angel": [22, 2],
                    "gemma": [13],
                    "marina": [27, 12]
                    }
for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"\n{name.title()}'s favorite number is:")
        for number in numbers:
            print(f"\t{number}")
    else:
        print(f"\n{name.title()}'s favorite numbers are:")
        for number in numbers:
            print(f"\t{number}")
        
    