# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1 + name2
lower_case_string = combined_string.lower()

# count letters for TRUE (without any loops... yet)
first_digit = lower_case_string.count('t') 
first_digit += lower_case_string.count('r')
first_digit += lower_case_string.count('u')
first_digit += lower_case_string.count('e')

# count letters for LOVE (without any loops... yet)
second_digit = lower_case_string.count('l') 
second_digit += lower_case_string.count('o') 
second_digit += lower_case_string.count('v') 
second_digit += lower_case_string.count('e') 

score = int( str(first_digit) + str(second_digit) )

# show score
message = ""

if score < 10 or score > 90:
    message = ", you go together like coke and mentos"
elif score >= 40 and score <= 50:
    message = ", you are alright together"

print(f"Your score is {score}{message}.")