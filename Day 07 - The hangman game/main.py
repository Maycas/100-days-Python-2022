import os
import random
from hangman_art import STAGES, LOGO
from hangman_words import word_list

# Game setup
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# Game start
print(LOGO)

# Testing code
#  print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

#  Ongoing game
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #  Clear console to give a better UX
    os.system('clear')

    #  Check if the guess was already guessed before
    if guess in display:
        print(f"You've already guessed {guess}")
    else:
        # Guess not guessed before,
        # Update display in case the letter exists
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # If the user is wrong, lose a life and check if he lost all lives
        if guess not in chosen_word:
            print(
                f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(
                    f"You lose... the word you wanted to find is {chosen_word}")

    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(STAGES[lives])
