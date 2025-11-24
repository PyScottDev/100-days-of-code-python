from coffee_data import MENU

def main_loop():
    choice = coffee_choice()
    sufficient = sufficient_resouces(choice)
    if not sufficient:
        return  # stop now, go back to main loop (ChatGPT Help)
    total_due = process_coins(sufficient)
    coffee_ready = check_transaction(choice, total_due)
    make_coffee(coffee_ready, choice)



# Prompt user about what they want
def coffee_choice():
    choice = input("What would you like? espresso, latte or cappuccino?").lower()
    if choice == "report":
        print(f"\nWater: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}\nMoney: ${resources["money"]}\n")
        #main_loop() # first attempt
        return coffee_choice() # ChatGPT edit
    elif choice == "off":
        #machine_off = True
        print("Goodbye!")
        quit()
    else:
        return choice


# Check that there are sufficient resources for the drink
def sufficient_resouces(choice):
    water = MENU[choice]["ingredients"]["water"]
    if choice != "espresso":
        milk = MENU[choice]["ingredients"]["milk"]
    else:
        milk = 0
    coffee = MENU[choice]["ingredients"]["coffee"]

    if water > resources["water"]:
        print("Sorry, there isn't enough water")
        return False
    elif milk > resources["milk"]:
        print("Sorry, there isn't enough milk")
        return False
    elif coffee > resources["coffee"]:
        print("Sorry, there isn't enough coffee")
        return False

    else:
        return True


#Process coins
def process_coins(sufficient):
    while sufficient == True:
        print("Insert coins:\n")
        quarters = float(input("How many quaters?: "))
        dimes = float(input("How many dimes?: "))
        nickles = float(input("How many nickles?: "))
        pennies = float(input("How many pennies?: "))
        total_due = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
        return total_due

def check_transaction(choice, amount):
    if amount < MENU[choice]["cost"]:
        print("Sorry, that's not enough money.  Money refunded")
        return False
    elif amount == MENU[choice]["cost"]:
        print(f"You inserted ${amount}.")
        resources["money"] += amount
        return True
    else:
        #change_due = amount - MENU[choice]["cost"]
        print(f"Here is ${amount - MENU[choice]["cost"]:.2f} in change.")
        resources["money"] += amount
        return True


#Make coffee. Deduct resources
def make_coffee(coffee_ready, choice):
    while coffee_ready == True: 
        print(f"Here's your {choice}. Have a nice day")
        resources["water"] -= MENU[choice]["ingredients"]["water"]
        if choice != "espresso":
            resources["milk"] -= MENU[choice]["ingredients"]["milk"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
        coffee_ready = False
        main_loop()

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 2.50,
}

machine_off = False

while machine_off == False:
    main_loop()