# Exercise 4.3 - Rock Paper Scissors
# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1

rock_draw = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_draw = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors_draw = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇

# Import the random module.
import random

# Define a variable acording to each number
rock = 0
paper = 1
scissors = 2

# Extract user's answer
your_answer = int(
    input(
        f"What do you choose? Type 0 for Rock, {paper} for Paper or {scissors} for Scissors."
    )
)

# Generate robot's answer
robot_answer = random.randint(0, 2)
print(robot_answer)

# Create an if/elif/else statement to check all the posibilities
if your_answer == rock:
    if robot_answer == 1:
        print(f"{rock_draw} \n Computer chose: {paper_draw}\n You lose")
    if robot_answer == 2:
        print(f"{rock_draw} \n Computer chose: {scissors_draw}\n You win")
    elif robot_answer == rock:
        print("This was a tie, please try again.")

if your_answer == paper:
    if robot_answer == rock:
        print(f"{paper_draw} \n Computer chose: {rock_draw}\n You win")
    if robot_answer == scissors:
        print(f"{paper_draw} \n Computer chose: {scissors_draw}\n You lose")
    elif robot_answer == paper:
        print("This was a tie, please try again.")

if your_answer == scissors:
    if robot_answer == rock:
        print(f"{scissors_draw} \n Computer chose: {rock_draw}\n You lose")
    elif robot_answer == paper:
        print(f"{scissors_draw} \n Computer chose: {paper_draw}\n You win")
    elif robot_answer == scissors:
        print("This was a tie, please try again.")
