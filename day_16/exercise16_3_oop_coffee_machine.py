# Exercise16_1 OOP Coffee Machine

from exercise16_3_oop_coffee_machine_menu import Menu, MenuItem
from exercise16_3_oop_coffee_machine_coffee_maker import CoffeeMaker
from exercise16_3_oop_coffee_machine_money_machine import MoneyMachine

machine_working = True
while machine_working:
    menu_available = Menu()
    availability = menu_available.get_items()

    order = input(f"What would you like?({availability}): ").lower()

    new_coffee = CoffeeMaker()
    money = MoneyMachine()
    if order == "off":
        print("Sorry 😓, this function is not available.")
        machine_working = False
    elif order == "report":
        new_coffee.report()
        money.report()
    else:
        enough_resources = new_coffee.is_resource_sufficient(
            menu_available.find_drink(order)
        )
        if enough_resources:
            payment = money.make_payment(menu_available.find_drink(order).cost)
            if payment:
                new_coffee.make_coffee(menu_available.find_drink(order))
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough resources for this order.")
            machine_working = False
