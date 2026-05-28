# Lottery🤑
from random import choice

lottery = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "a", "b", "c", "d", "e"]

choosen_numbers = []
print(f" Any ticket matching the next four numbers wins a prize of $1.000.000 dollars!!!")

while len(choosen_numbers) < 4:
    number = choice(lottery)
    if number not in choosen_numbers:
        print(f"We pulled a {number} from the lottery machine")
        choosen_numbers.append(number)

print(f"The winning ticket is... {choosen_numbers}")