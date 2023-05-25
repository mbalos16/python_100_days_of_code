# Exercise 13.1 - Debugging odd or even

# Instructions
#     Read this the code in main.py
#     Spot the problems 🐞.
#     Modify the code to fix the program.
# Fix the code so that it works and passes the tests when you submit.

# Initial code: 
#     number = int(input("Which number do you want to check?"))

# if number % 2 = 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

# Solution
number = int(input("Which number do you want to check?"))
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  