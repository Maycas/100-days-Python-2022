from menu import MENU
from resources import INITIAL_RESOURCES


def print_report(resources):
    """
    Prints a report with available resources and profit
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['profit']}")


def is_resource_sufficient(resources, ingredients):
    """
    Returns True when an order can be made. False if ingredients are not sufficient
    """
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def process_coins():
    """
    Returns the total amount of inserted coins
    """
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost, resources):
    """
    Returns True when the payment is accepted, or false if money is insufficient
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here's ${change} in change.")
        resources['profit'] += drink_cost
        return True
    else:
        print("Sorry. That's not enough money. Money refunded")
        return False


def make_coffee(drink_name, ingredients, resources):
    """
    Deduct ingredients from the resources
    """
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def coffee_machine():
    """
    Operates the coffee machine
    """
    machine_is_on = True
    resources = INITIAL_RESOURCES

    while machine_is_on:
        option = input("What would you like (espresso / latte / cappuccino)? ").lower()

        if option == 'off':
            machine_is_on = False
        elif option == 'report':
            print_report(resources)
        else:
            try:
                drink = MENU[option]
                if is_resource_sufficient(resources, drink['ingredients']):
                    payment = process_coins()
                    if is_transaction_successful(payment, drink['cost'], resources):
                        make_coffee(option, drink['ingredients'], resources)
            except Exception as e:
                print(f"Option {e} not available. Please try again")


coffee_machine()
