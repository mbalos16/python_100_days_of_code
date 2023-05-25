# Exercise 12.1 Guess the number

import random
from art_exercise_12_1_guess_the_number import logo

# Print logo and welcome message
print(logo)
print(
    "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100."
)

# Generate a random number that the user needs to guess.
number_in_mind = random.randint(1, 100)

# Code used just for testing
# print(f"Pssssss. The correct number is {number_in_mind}")

# Ask the user for the dificulty level.
game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Determine the attempts based on the dificulty number.
attempts = 0
if game_level == "easy":
    attempts = 10
else:
    attempts = 5


# Asking the user to guess while there are still atempts.
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess == number_in_mind:
        print(f"🎉🎉🎉 You got it 🎯. The answer was {number_in_mind}.")
        break
    elif user_guess > number_in_mind:
        print("Too high.")

    elif user_guess < number_in_mind:
        print("Too low.")

    attempts -= 1
    if attempts != 0:
        print("Guess again.")

if attempts == 0:
    print("🤦‍♀️🤦‍♀️🤦‍♀️ You've run out of guesses, you lose. 😭")
