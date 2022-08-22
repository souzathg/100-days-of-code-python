from art import logo
import random

def compare(guess, secret_number):
    if guess < secret_number:
        return 0
    elif guess > secret_number:
        return 2
    else:
        return 1

print(logo)
print("Welcome to the guessing number game!")

print("I'm thinking of a number between 1 and 100.")
secret_number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 0

if difficulty == 'easy':
    attempts += 10
else:
    attempts += 5

while attempts > 0:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))

    comparison = compare(guess, secret_number)

    if comparison == 0:
        print("Too low.")
        print("Guess again.")
    elif comparison == 2:
        print("Too high.")
        print("Guess again.")
    else:
        break

    attempts -= 1

if attempts == 0:
    print("You've run out of guesses, you lose.")
    print(f"The secret number was {secret_number}.")
else:
    print(f"You got it! The answer was {secret_number}.")
