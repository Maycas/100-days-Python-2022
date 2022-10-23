# Simple function
def greet():
    print("Hello Angela")
    print("How do you do?")
    print("Isn't the weather nice today?")

# greet()

# Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"How do you do {name}?")
    print("Isn't the weather nice today?")

# greet_with_name("Marc")
# greet_with_name("Clara")

# Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# greet_with("Angela", "London")
# greet_with("London", "Angela") # complete nonsense as it takes the position of the data and here it is assigned incorrectly

greet_with(location = "London", name = "Angela") # using keyword arguments