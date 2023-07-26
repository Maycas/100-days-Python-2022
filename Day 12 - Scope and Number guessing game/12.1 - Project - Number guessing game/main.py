from random import randint
from art import LOGO

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0


def check_answer(guess, answer, turns):
    """
    Checks answer against guess. Returns the number of turns remaining
    """
    if guess > answer:
        print("Too high...")
        return turns - 1
    elif guess < answer:
        print("Too low...")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}!")


def set_difficulty():
    """
    Return number of turns to use depending on chosen difficulty
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    """
    Plays a "Guess the Number!" game
    """
    print(LOGO)
    print("Welcome to the Guessing Game!")
    print("I'm thinking on a number between 1 and 100.")

    # Choose a random number between 1 and 100
    answer = randint(1, 100)
    # print(f"Psst, the correct answer is {answer}")

    turns = set_difficulty()

    # Repeat guessing if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        # Let the user guess the number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they got it wrong
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose")
            return


game()
