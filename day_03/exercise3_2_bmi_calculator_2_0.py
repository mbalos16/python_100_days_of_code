# Exercise 3.2 - BMI calculator 2.0

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
#     Under 18.5 they are underweight
#     Over 18.5 but below 25 they have a normal weight
#     Over 25 but below 30 they are slightly overweight
#     Over 30 but below 35 they are obese
#     Above 35 they are clinically obese.

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = float(weight) / float(height) ** 2
bmi = round(bmi)

# Same code with bold names integrated in the code
# class color:
#    BOLD = '\033[1m'
#    END = '\033[0m'
# if bmi < 18.5:
#     print("Your BMI is "+ str(bmi) +", you are " + color.BOLD + "underweight" + color.END+ ".")
# elif bmi >= 18.5 and bmi < 25:
#         print("Your BMI is "+ str(bmi) +", you have a " + color.BOLD + "normal weight" + color.END + ".")
# elif bmi >= 25 and bmi < 30:
#     print("Your BMI is "+ str(bmi) +", you are slightly " + color.BOLD + "overweight" + color.END + ".")
# elif bmi >= 30 and bmi < 35:
#     print("Your BMI is "+ str(bmi) +", you are  " + color.BOLD + "obese" + color.END + ".")
# else:
#     print("Your BMI is "+ str(bmi) +", you are  " + color.BOLD + "clinically obese" + color.END + ".")


if bmi < 18.5:
    print("Your BMI is " + str(bmi) + ", you are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print("Your BMI is " + str(bmi) + ", you have a normal weight.")
elif bmi >= 25 and bmi < 30:
    print("Your BMI is " + str(bmi) + ", you are slightly overweight.")
elif bmi >= 30 and bmi < 35:
    print("Your BMI is " + str(bmi) + ", you are obese.")
else:
    print("Your BMI is " + str(bmi) + ", you are clinically obese.")
