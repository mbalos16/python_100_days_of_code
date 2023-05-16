# Password Generator Project


# Go to: https://replit.com/@appbrewery/password-generator-start?v=1

import random
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = []
# We allow the loop to go through the list from 0 until the number of letters defined by the user.
for leter in range(0, nr_letters):
    # We generate a random number between o and the total lenght of the letters list - 1 to pass it as a position from the list.
    # We actualize the password with the given letter.
    password += letters[random.randint(0, (len(letters) - 1))]

for symbol in range(0, nr_symbols):
    password += symbols[random.randint(0, (len(symbols) - 1))]

for number in range(0, nr_numbers):
    password += numbers[random.randint(0, (len(numbers) - 1))]
# print(f" Your password: {password}")


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
str(random.shuffle(password))
password_new = ""
for character in password:
    password_new += character
print(password_new)
