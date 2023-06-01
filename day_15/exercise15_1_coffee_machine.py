# Exercise15_1 Coffee Machine

# Instructions
# 1. Prompt user by asking “​What would you like? (espresso/latte/cappuccino):”​
#     a. Check the user’s input to decide what to do next.
#     b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
# 2. Turn off the Coffee Machine by entering “​off”​to the prompt.
#     a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
# 3. Print report.
#     a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
#         Water: 100ml
#         Milk: 50ml
#         Coffee: 76g
#         Money: $2.5
# 4. Check resources sufficient?
#     a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
#     b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “​Sorry there is not enough water.”​
#     c. The same should happen if another resource is depleted, e.g. milk or coffee.
# 5. Process coins.
#     a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
#     b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#     c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# 6. Check transaction successful?
#     a. Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “​Sorry that's not enough money. Money refunded.​”.
#     b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g. Water: 100ml
#         Milk: 50ml[]
#         Coffee: 76g
#         Money: $2.5
#     c. If the user has inserted too much money, the machine should offer change.
#         E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
# 7. Make Coffee.
#     a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
#         E.g. report before purchasing latte: Water: 300ml
#         Milk: 200ml
#         Coffee: 100g
#         Money: $0
#         Report after purchasing latte:
#                 Water: 100ml
#                 Milk: 50ml
#                 Coffee: 76g
#                 Money: $2.5
#     b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.


# Import exterior data and print the logo
from data_exercise15_1_coffee_machine import MENU, resources
from art_exercise15_1_coffee_machine import logo

print(logo)

# We define a boolean value that helps us to turn off the machine when is not needed or don't have enough resources.
machine_working = True
orders = 0


# We generate the coffee machine report taking into acount if there were customers using the machine or not.
def create_report(resources):
    for key in resources:
        print(f"{key} : {resources[key]}")


# Update the resources baed on users choice
def rest_resources(user_choice, MENU, resources):
    if "water" in MENU[user_choice]["ingredients"]:
        resources["water"] -= MENU[user_choice]["ingredients"]["water"]
    if "milk" in MENU[user_choice]["ingredients"]:
        resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
    if "coffee" in MENU[user_choice]["ingredients"]:
        resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
    resources["money"] += MENU[user_choice]["cost"]


# Ask for money in different values and return if there is a coffe or not.
def ask_for_money(user_choice, MENU, rest_resources):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    # Sum all the different money in one variable.
    sum = 0
    for quarter in range(0, quarters):
        sum += 0.25
    for dime in range(0, dimes):
        sum += 0.10
    for nickle in range(0, nickles):
        sum += 0.05
    for penni in range(0, pennies):
        sum += 0.01

    # Check if there is enough money and if so prints the result.
    if sum >= MENU[user_choice]["cost"]:
        change = sum - MENU[user_choice]["cost"]
        if change > 0:
            print(
                f"Here is ${change:.2f} in change.\nHere is your {user_choice}. Enjoy!"
            )
        else:
            print(f"Here is your {user_choice}. Enjoy!")

        rest_resources(user_choice, MENU, resources)
        resources["money"] += sum
    else:
        print("Sorry that's not enough money. Money refunded.")


# Check if there are enough resources to make the coffee
def check_resources(MENU, resources, user_choice, order, machine_working):
    if order == 0:
        machine_working = True
    else:
        if MENU[user_choice]["ingredients"]["water"] > resources["water"]:
            print("Sorry, there is not enough water.")
            machine_working = False
        if MENU[user_choice]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, there is not enough coffee.")
            machine_working = False
        if MENU[user_choice]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry, there is not enough milk.")
            machine_working = False
        else:
            return machine_working
    return machine_working


# While the machine is still on and has resources still working
while machine_working:
    # Ask user for the chosen preference
    user_choice = input("What would you like? (espresso\latte\cappuccino): ").lower()

    # Turn off the machine
    if user_choice == "off":
        print("This system is out of coffeine. I'm going to have a loooonnnng nap 😴.")
        machine_working = False

    # User chose report so we print the up to date machine report
    elif user_choice == "report":
        create_report(resources)

    # User chose espresso
    elif (
        user_choice == "espresso"
        or user_choice == "latte"
        or user_choice == "cappuccino"
    ):
        check_resources(MENU, resources, user_choice, orders, machine_working)
        ask_for_money(user_choice, MENU, rest_resources)
        orders += 1

    else:
        print(f"Sorry the {user_choice} option is not available for now.")
