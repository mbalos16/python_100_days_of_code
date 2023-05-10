# Exercise 2.3 - Life in weeks

# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
# https://waitbutwhy.com/2014/05/life-weeks.html
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format: You have x days, y weeks, and z months left.
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
# Where x, y and z are replaced with the actual calculated numbers.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
year = 365
weeks = 52
months = 12
expected_age = 90

your_days = int(year) * int(expected_age) - int(year) * int(age)
your_weeks = int(weeks) * int(expected_age) - int(weeks) * int(age)
your_months = int(months) * int(expected_age) - int(months) * int(age)

print(f"You have {your_days} days, {your_weeks} weeks, and {your_months} months left.")
