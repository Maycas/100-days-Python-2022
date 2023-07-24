print("Hello World!")

print("Hello World!\nHello World!\nHello World!")  # several lines with \n

print("Hello " + "Marc")
print("Hello" + " " + "Marc")
print("Hello", "Marc")  # careful with the missing space

print("Hello " + input("What is your name? ") + "!")

name = input("What's your name? ")
print("Hello " + name)
print("Your name is " + str(len(name)) + " characters long")
