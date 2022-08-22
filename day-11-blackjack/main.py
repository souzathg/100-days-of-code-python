import os
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(cards):
    return random.choice(cards)

def calculate_score(hand):
    if len(hand) == 2 and sum(hand) == 21:
        return 0
    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return 1
    if computer_score == 0:
        return 0
    if user_score == 0:
        return 2
    if user_score > 21:
        return 0
    if computer_score > 21:
        return 2
    if computer_score > user_score:
        return 0
    return 2

os.system("clear")
keep_playing = True

while keep_playing:
    user_turn = True
    game_over = False

    print(logo)

    user_cards = []
    computer_cards = []

    for i in range(0, 2):
        user_cards.append(deal_card(cards))
        computer_cards.append(deal_card(cards))

    while user_turn:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards are: {user_cards}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
            break

        draw_card_question = input("Do you want to draw another card? Type 'y' for yes, 'n' for no: ")

        while draw_card_question != 'y' and draw_card_question != 'n':
            draw_card_question = input("Please, type 'y' or 'n': ")

        if draw_card_question == 'y':
            user_cards.append(deal_card(cards))
            os.system("clear")
        elif draw_card_question == 'n':
            user_turn = False
            continue

    while computer_score < 17 and not game_over:
        computer_cards.append(deal_card(cards))
        computer_score = calculate_score(computer_cards)

    result = compare(user_score=user_score, computer_score=computer_score)

    if result == 0:
        print("The dealer wins!")
    elif result == 1:
        print("It's a draw.")
    else:
        print("You win!")

    print(f"The dealer cards were: {computer_cards}")

    keep_playing_question = input("Do you want to keep playing? Type 'y' for yes, 'n' for no: ")

    while keep_playing_question != 'y' and keep_playing_question != 'n':
            keep_playing_question = input("Please, type 'y' or 'n': ")

    if keep_playing_question == 'n':
        keep_playing = False
    else:
        os.system("clear")
