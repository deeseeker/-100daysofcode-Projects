from art12 import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

numbers = [*range(0,101)]
guess = random.choice(numbers)
print("Pssst", f"the correct number is {guess}")



def easy_level():
    n=10
    while n > 0:
        user_guess = int(input("Make a guess: "))
        if user_guess > guess:
            print("Too high.")
            print("Guess again.")
            n -= 1
            print(f"You have {n} attempts left")
        elif user_guess < guess:
            print("Too low.")
            print("Guess again.")
            n -= 1
            print(f"You have {n} attempts left")
        else:
            print(f"You got it! The answer was {guess}")
            break
def hard_level():
    n=5
    while n > 0:
        user_guess = int(input("Make a guess: "))
        if user_guess > guess:
            print("Too high.")
            print("Guess again.")
            n -= 1
            print(f"You have {n} attempts left")
        elif user_guess < guess:
            print("Too low.")
            print("Guess again.")
            n -= 1
            print(f"You have {n} attempts left")
        else:
            print(f"You got it! The answer was {guess}")
            break


level_choice = input("Choose a difficulty. Type 'easy' or 'hard':")

if level_choice == 'easy':
    easy_level()
elif level_choice == 'hard':
    hard_level()
