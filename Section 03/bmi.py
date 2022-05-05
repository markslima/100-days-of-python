# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# "Your BMI is 18, you are underweight."
# "Your BMI is 22, you have a normal weight."
# "Your BMI is 28, you are slightly overweight."
# "Your BMI is 33, you are obese."
# "Your BMI is 40, you are clinically obese."

# BMI = WEIGHT / HEIGHT **2 
bmi = round(weight / height ** 2)

# print(bmi)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"You BMI is {bmi}, you are normal weight.")
elif bmi < 28:
    print(f"Your BMI is {bmi}, you are slight overweight.")
elif bmi < 33:
    print(f'Your BMI is {bmi}, you are obese.')
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

