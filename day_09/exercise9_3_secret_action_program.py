# Exercise 9.3 Secret Action Program

from replit import clear

# HINT: You can call clear() to clear the output in the console.
bidders = {}
more_bidders = True

# While there is still bidders in the room we still run the code.
while more_bidders:
    name = input("What is your name: ")
    bid = int(input("What's your bid: "))
    other = input("Are there any other bidders? Type 'yes'or 'not'\n").lower()

    # Update the bidders dictionary
    bidders[name] = bid

    # Check if there are more bidders
    if other == "not":
        more_bidders = False
    if other == "yes":
        clear()

# Get the highest bidder
highest_bidder = ""
highest_bid = 0
for key in bidders:
    if bidders[key] > highest_bid:
        highest_bidder = key
        highest_bid = bidders[key]

# Print the result
print(f"The winner is {highest_bidder} with a bid of {highest_bid}.")
