# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        leap = False
    else:
        leap = True
else:
    leap = False

if leap:
    print("Leap year.")
else:
    print("Not leap year.")