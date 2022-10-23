#Data Types

#String
print("Hello"[0]) # extract first character
print("Hello"[4]) # last character
print("Hello"[-1]) # another way to get the last character

#Integer
print(123 + 345)

#Float
print(3.14169)

#Boolean
True
False

#Casting or Type Conversion
num_char = len(input("What is your name? ")) # this returns an integer
num_char_str = str(num_char) # convert to string
print("Your name has " + num_char_str + " characters") # now we can concatenate strings and numbers

a = 123
print(type(a)) # integer

a = str(123)
print(type(a)) # string

a = float(123)
print(type(a)) # float

print(70 + float("100.5")) # 170.5
print(str(70) + str(100)) # 70100

#Mathematical operations
print(3 + 5)
print(7 - 4)
print(3 * 2)
print(3 // 2) # integer division

print(6 / 3) # returns 2.0, a float
print(type(6 / 3))

print (2 ** 4)

# PEMDASLR order of operations (Parenthesis, Exponents, Multiplication, Division, Addition, Subtraction, from Left to Right)
print(3 * 3 + 3 / 3 - 3) # 9 + 1 - 3 = 7
print(3 * (3 + 3) / 3 - 3 ) # 3 * 6 / 3 - 3 = 18 / 3 - 3 = 6 - 3 = 3

# Update score values using mathematical operators in a simpler and more convenient way
score = 100
score += 10
score /= 2
score *= 3
score -= 50

# f-Strings
score = 10
height = 1.9
is_winning = True
print(f"Your score is {score}, your height is {height}, you are winning is {is_winning}")
