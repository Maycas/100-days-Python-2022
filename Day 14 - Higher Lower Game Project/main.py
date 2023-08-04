import os
import random
from art import LOGO, VS
from game_data import data


def format_data(option):
    """ Format the option data into a printable format """
    return f"{option['name']}, a {option['description']}, from {option['country']}. ({option['follower_count']})"


def check_user_guess(guess, option_a, option_b):
    """ Take users guess and the selected options to check if the user got it right """
    if option_a['follower_count'] > option_b['follower_count']:
        return guess == 'A'
    else:
        return guess == 'B'


def game():
    score = 0
    game_should_continue = True

    # Setting option B first, so it becomes option A later so we can repeat that option A becomes option B if the user guesses right
    option_b = random.choice(data)

    print(LOGO)

    # Make the game repeatable
    while game_should_continue:
        # Making option B to become option A if the user got it right
        option_a = option_b
        option_b = random.choice(data)

        # Make sure the 2 options are different
        while option_a == option_b:
            option_b = random.choice(data)

        # Format and print each option (option A + VS + Option B)
        print(f"Compare A: {format_data(option_a)}")
        print(VS)
        print(f"Against B: {format_data(option_b)}")

        # Ask player for who has more followers and expect an input
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        #  Check correct guess
        is_correct = check_user_guess(guess, option_a, option_b)

        # Clear screen between rounds
        os.system('clear')
        print(LOGO)

        # Give user feedback on their guess and keep track of score
        if is_correct:
            score += 1
            print(f"You are right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")


game()
