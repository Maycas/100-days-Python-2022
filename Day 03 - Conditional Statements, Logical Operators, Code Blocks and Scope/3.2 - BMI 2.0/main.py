# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = round(float(weight) / float(height) ** 2)

if bmi < 18.5:
    condition = "are underweight"
elif bmi < 25:
    condition = "have a normal weight"
elif bmi < 30:
    condition = "are slightly overweight"
elif bmi < 35:
    condition = "are obese"
else:
    condition = "are clinically obese"

print(f"Your BMI is {bmi}, you {condition}")
