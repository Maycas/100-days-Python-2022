fruits = ["Apple", "Peach", "Pear"]

# For loops - Print items 1 by 1
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# Range function
for number in range(1, 10):
    print(number)  # won't print last number

# Add all numbers from 1 to 101
accumulator = 0
for number in range(1, 101):
    accumulator += number
print(accumulator)
