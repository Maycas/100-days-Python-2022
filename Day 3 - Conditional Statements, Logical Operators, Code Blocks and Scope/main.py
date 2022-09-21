# If / Else
## Example 1 - Shall we drain the water in the bathtub?
water_level = 50
if water_level > 80:
    print("Drain Water")
else:
    print("Continue")

## Example 2 - Can I ride the rollercoaster?
print("Welcome to the rollercoaster")
height = int( input("What is your height in cm? ") )

if height >=  120:
    print("You can ride the rollercoaster")
else:
    print("Sorry, you have to grow taller before you can ride")

# Example 3 - Nested if / else
print("Welcome to the rollercoaster")
height = int( input("What is your height in cm? ") )

if height >=  120:
    print("You can ride the rollercoaster")
    age = int( input("What is your age? ") )
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride")

# Example 4 - elif
print("Welcome to the rollercoaster")
height = int( input("What is your height in cm? ") )

if height >=  120:
    print("You can ride the rollercoaster")
    age = int( input("What is your age? ") )
    if age < 12:
        print("Please pay $5.")
    elif age < 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride")