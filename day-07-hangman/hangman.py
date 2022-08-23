import random
import hangman_art as art
import hangman_words as words
import os
from sys import platform

word_list = words.word_list
stages = art.stages
logo = art.logo

chosen_word = random.choice(word_list)

lives = 6

display = []

for number in range(len(chosen_word)):
    display.append("_")

print(f"{logo}")

print(f"The chosen word is: {chosen_word}")

print(f"{' '.join(display)}")

game_over = False
print(stages[lives])

guesses = []

while not game_over:

    guess = input("Please, guess a letter: ").lower()

    if platform == "linux" or platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")

    letters_filled = 0

    for index in range(len(chosen_word)):
        if guess == chosen_word[index]:
            display[index] = guess
            letters_filled += 1

    if letters_filled == 0 and guess not in guesses:
        lives -= 1

    print(stages[lives])

    print(f"{' '.join(display)}\n")

    if guess in guesses:
        print("You've already guessed that letter!\n")

    if lives == 0:
        break

    if guess not in guesses:
        guesses.append(guess)

    print(f"Letters guessed: {guesses}")

    # Game is only over when all of the letters are filled
    if "_" not in display:
        game_over = True

if lives == 0:
    print(f"You lose! The word was '{chosen_word}'.")
else:
    print("You've won! Congratulations!")
