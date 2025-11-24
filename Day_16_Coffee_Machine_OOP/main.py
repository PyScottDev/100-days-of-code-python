from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_off = False

while is_off == False: 
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_off = True
    else:
        order = menu.find_drink(choice)
        sufficient_resources = coffee_maker.is_resource_sufficient(order)
        cost_of_drink = order.cost
        money_received = money_machine.make_payment(cost_of_drink)
        coffee_maker.make_coffee(order)