# Guessing number game using while loops
import random

hidden_number = random.randint(1, 100)

user_number = 0

while not user_number == hidden_number:
    user_number = int(input("Guess a number between 1 and 100:"))
    if user_number > hidden_number:
        print("Too high!Try again")
    elif user_number < hidden_number:
        print("Too low! Try again")
    else:
        print("You got that right!")
        print()