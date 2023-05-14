# Exercise 3.5 - Love calculator

# Instructions
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
#     Take both people's names and check for the number of times the letters in the word TRUE occurs.
#     Then check for the number of times the letters in the word LOVE occurs.
#     Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
names_together = name1.lower() + name2.lower()
# print(names_together)

t = 0
r = 0
u = 0
e = 0

l = 0
o = 0
v = 0
e2 = 0

# Counting each carracter fron true love text in the two names
if names_together.count("t") > 0:
    t += names_together.count("t")

if names_together.count("r") > 0:
    r += names_together.count("r")

if names_together.count("u") > 0:
    u += names_together.count("u")

if names_together.count("e") > 0:
    e += names_together.count("e")


if names_together.count("l") > 0:
    l += names_together.count("l")

if names_together.count("o") > 0:
    o += names_together.count("o")

if names_together.count("v") > 0:
    v += names_together.count("v")

if names_together.count("e") > 0:
    e2 += names_together.count("e")

# We know that the score is the main results fron true and love together in percentage.
score_first_number = t + r + u + e
score_second_number = l + o + v + e2
score = str(score_first_number) + str(score_second_number)
score_int = int(score)

# Message based on score
if score_int < 10 or score_int > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score_int >= 40 and score_int <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
