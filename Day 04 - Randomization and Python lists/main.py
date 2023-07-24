# RANDOMNESS
import random
import my_module  # custom module we created

print(my_module.pi)  # printing a value

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

# How to print a random float between 0 and 5 (but not including 5)?
random_float = random.random() * 5
print(random_float)

# What are the uses for random numbers
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# LISTS
states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]
print(states_of_america[0])
print(states_of_america[-1])

# change a value in a list
states_of_america[1] = "Pencilvania"
print(states_of_america)

# add items in the list
states_of_america.append("Angelaland")
print(states_of_america)

# extending a list
states_of_america.extend(["Jack Bauer Land, Disneyland, Super Mario Land"])
print(states_of_america)

# nested lists
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]  # a list made of 2 lists
print(dirty_dozen)
