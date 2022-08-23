print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

game_over = False

choice = input("You're at a crossroads. Do you go left or right?\n").lower()

if choice == "left":
    print("You got past a hole that you've fallen if you headed right. Good job!\nNow, you walk until you see a calmy looking river, at first.")
    choice = input("Do you wait to see what happens or do you swim to the other side?\n").lower()

    if choice == "wait":
        print("Suddenly, the river starts disappearing and you are presented to three doors. A red one, a yellow one and a blue one.")
        choice = input("Which one are you going to open?\nRed, yellow or blue?\n").lower()

        if choice == "yellow":
            print("Contratulations! You win! The treasure is yours!")
        elif choice == "red":
            print("You got burned by fire. Gave over!")
        elif choice == "blue":
            print("You got eaten by beasts. Game over!")
        else:
            print("Game over.")
    elif choice == "swim":
        print("You got attacked by trouts. Game over!")
    else:
        print("Game over!")
else:
    print("You fell into a hole! Game over!")
