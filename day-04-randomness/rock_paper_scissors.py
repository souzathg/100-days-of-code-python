import random
import rps_figures as rps

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

figures = [rps.rock, rps.paper, rps.scissors]

print(figures[player_choice])
print("Computer chose:")
print(figures[computer_choice])

if player_choice == 0:
    if computer_choice == player_choice:
        print("It's a draw.")
    elif computer_choice == 1:
        print("You lose.")
    elif computer_choice == 2:
        print("You win.")
elif player_choice == 1:
    if computer_choice == player_choice:
        print("It's a draw.")
    elif computer_choice == 2:
        print("You lose.")
    elif computer_choice == 0:
        print("You win.")
elif player_choice == 2:
    if computer_choice == player_choice:
        print("It's a draw.")
    elif computer_choice == 0:
        print("You lose.")
    elif computer_choice == 1:
        print("You win.")
