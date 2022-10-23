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

# Example 4 - elif (several prices depending on age)
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

# Example 5 - Multiple if statements
print("Welcome to the rollercoaster")
height = int( input("What is your height in cm? ") )
bill = 0

if height >=  120:
    print("You can ride the rollercoaster")
    age = int( input("What is your age? ") )
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets $12.")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        # Add $3 to their bill
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride")

# Example 6 - Logical operators
# Free ride for people aged 45 - 55 (people with midlife crisis)
print("Welcome to the rollercoaster")
height = int( input("What is your height in cm? ") )
bill = 0

if height >=  120:
    print("You can ride the rollercoaster")
    age = int( input("What is your age? ") )
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be Ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets $12.")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        # Add $3 to their bill
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride")