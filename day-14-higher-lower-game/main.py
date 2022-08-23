from art import *
from game_data import data
import random
import os
import platform


def compare(A, B):
    if A['follower_count'] > B['follower_count']:
        return 'A'
    return 'B'


def clear():
    if platform == "win32":
        return os.system("cls")
    return os.system("clear")


while True:
    A = random.choice(data)
    score = 0

    while True:
        B = random.choice(data)
        while A == B:
            B = random.choice(data)

        clear()

        print(logo)
        if score > 0:
            print(f"You're right! Current socre: {score}.")
        print(f"A: {A['name']}, a {A['description']}, from {A['country']}.")
        print(vs)
        print(f"B: {B['name']}, a {B['description']}, from {B['country']}.")

        highest_followers = compare(A, B)

        guess = input("Who has more followers? Type 'A' or 'B': ")

        if guess == highest_followers:
            A = B
            score += 1
        else:
            break

    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")

    if input("Do you want to play again? Type 'y' or 'n': ") == 'n':
        break
