from game_data import data
from art import logo, vs
import random

#my solution to the problem
# create a function to generate the value

def selector():
    value = random.choice(data)
    name = value["name"]
    description = value["description"]
    country = value["country"]
    follower = value['follower_count']
    return name, description, country, follower




def compare(fca,fcb):
    if fca > fcb:
        return 'a'
    else:
        return 'b'
def end_game(user_choice,A,B):
    answer = compare(A[3],B[3])

    if user_choice.lower() != answer:
        return True






# start
def play_game():
    print(logo)
    final_score = 0
    A = selector()
    B = selector()
    print(f"Compare A: {A[0]}, a {A[1]}, from {A[2]}")
    print(vs)
    print(f"Against B: {B[0]}, a {B[1]}, from {B[2]}")

    choice = input("Who has more followers? Type 'A' or 'B': ")
    while not end_game(choice,A,B):
        final_score +=1
        A = B
        B = selector()
        print(f"Compare A: {A[0]}, a {A[1]}, from {A[2]}")
        print(vs)
        print(f"Against B: {B[0]}, a {B[1]}, from {B[2]}")
        choice = input("Who has more followers? Type 'A' or 'B': ")a

    print("Sorry, that's wrong.")

play_game()

#correction
