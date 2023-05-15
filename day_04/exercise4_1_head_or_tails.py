# Exercise 4.1 - Heads or Tails


# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
# There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.


# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲
import random

# Write the rest of your code below this line 👇
print('Welcome to the "Heads and tails" flip coin random generator!')

random_number = random.randint(0, 1)
# print(random_number)
if random_number == 1:
    print("You got a Head!")
elif random_number == 0:
    print("You got a Tail!")
