import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
options = [rock, paper, scissors]

# Player choice
player_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Computer choice
computer_choice = random.randint(0, 2)

# Determining the winner
#  Looking at how the options are structured. A player always beats the option on his left, and loses
# against the option on his right. So, if player - computer == 1, then the player wins. Then, if the
# player selects scissors and computer selects rock, then player the player loses
# (player - computer == 2). Finally, there's an edge case, where player selects rock and computer
# selects scissors, then player - computer = -2.
# In that last case, we need to convert this -2 using the modulo operator so it becomes a 1 and the
# player wins, so doing (player - computer) % 3 = 1, and then the player wins.

difference = (player_choice - computer_choice) % 3

if difference == 2:
    result = "You lose..."
elif difference == 1:
    result = "You win!"
elif difference == 0:
    result = "It's a tie!"

# Game output
try:
    # Protecting against invalid number typed by the user
    print(options[player_choice])
except:
    result = "You typed an invalid number, you lose"

print("Computer chose:\n", options[computer_choice])
print(result)
