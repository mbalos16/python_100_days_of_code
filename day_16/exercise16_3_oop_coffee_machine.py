# Exercise16_1 OOP Coffee Machine

from exercise16_3_oop_coffee_machine_menu import Menu, MenuItem
from exercise16_3_oop_coffee_machine_coffee_maker import CoffeeMaker
from exercise16_3_oop_coffee_machine_money_machine import MoneyMachine

machine_working = True
menu_available = Menu()
new_coffee = CoffeeMaker()
money = MoneyMachine()

while machine_working:
    availability = menu_available.get_items()
    order = input(f"What would you like?({availability}): ").lower()
    if order == "off":
        machine_working = False
    elif order == "report":
        new_coffee.report()
        money.report()
    else:
        enough_resources = new_coffee.is_resource_sufficient(
            menu_available.find_drink(order)
        )
        payment = money.make_payment(menu_available.find_drink(order).cost)
        if enough_resources and payment:
            new_coffee.make_coffee(menu_available.find_drink(order))
