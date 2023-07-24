############### Blackjack Project ######################################

############### Our Blackjack House Rules ##############################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
#  The dealer will keep requesting cards if its hand is lower than 17.

########################################################################

import os
import random
from art import LOGO


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(hand):
    """Take a list of cards and return the score calculated from the cards"""
    #  checking if the hand has a blackjack and modelling it as a 0
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    #  if the hand busted, replace an ace with value 11 with a 1
    if (11 in hand) and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)


def compare(user_score, computer_score):
    """Compares scores and returns the outcome of the game"""
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has a Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over, you lose 😭"
    elif computer_score > 21:
        return "Opponent went over, you win 😁"
    elif user_score > computer_score:
        return "You win 😀"
    else:
        return "You lose 😤"


def play_game():
    """Play a game of Blackjack"""
    print(LOGO)

    user_cards = []
    computer_cards = []
    is_game_over = False

    #  dealing initial hands
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #  play the game
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards: {user_cards}, current_score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}\n")

        # check end of game conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # if the game hasn't ended, ask the user what they want to do
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                # if the user finishes dealing, then the game ends
                is_game_over = True
                #  but the computer needs to keep getting cards if it is below 17
                while computer_score != 0 and computer_score < 17:
                    computer_cards.append(deal_card())
                    computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final_score: {user_score}")
    print(
        f"    Opponent's final hand: {computer_cards}, final_score: {computer_score}\n")
    print(compare(user_score, computer_score) + "\n")


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    os.system('clear')
    play_game()
