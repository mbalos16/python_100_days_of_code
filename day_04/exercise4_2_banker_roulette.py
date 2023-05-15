# Exercise 4.2 - Banker Roulette

# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name


# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

# Returns the list of names in list.
names_string = names.append(names)
# print(names)

# Returns the lenght of the list
list_lenght = len(names)
# print (list_lenght)

# Returns a random number between 0 and the length of the string.
random_number = random.randint(0,list_lenght)
# print(random_number)

# Return a name based on the random number. 
print(f"{names[random_number]} is going to buy the meal today!")