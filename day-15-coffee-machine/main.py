from menu import MENU

on = True

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def print_report(resources, profit):
    """
    Prints the machine's resources report.
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_resources(drink, resources):
    """
    Checks if there are enough resources to make a drink.
    """
    for key in drink["ingredients"]:
        if key in resources:
            if resources[key] < drink["ingredients"][key]:
                print(f"Sorry, there is not enough {key}.")
                return False
    return True


def process_coins():
    """
    Converts the sum of the coins to dollars
    """
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def check_money(drink, total_money):
    """
    Checks if the user has inserted more money than the drink's cost.
    If he hasn't inserted, it gives the money back.
    """
    if drink['cost'] > total_money:
        print(f"Sorry, that's not enough money. Money refunded.")
        return False
    return True


def calculate_change(drink, total_money):
    """
    Calculates the change based on the value inserted by the user.
    """
    change = total_money - drink['cost']
    print(f"Here is ${round(change, 2)} in change.")


def make_drink(drink, resources):
    """
    Subtracts the resources from the stock.
    """
    for key in drink["ingredients"]:
        if key in resources:
            resources[key] -= drink["ingredients"][key]


while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        on = False
        continue
    elif choice == "report":
        print_report(resources, profit)
        continue
    else:
        drink = MENU[choice]

    if not check_resources(drink, resources):
        continue

    print("Please, insert coins.")
    total_money = process_coins()

    if not check_money(drink, total_money):
        continue

    calculate_change(drink, total_money)
    make_drink(drink, resources)

    print(f"Here is your {choice} ☕. Enjoy!")
    profit += drink['cost']
