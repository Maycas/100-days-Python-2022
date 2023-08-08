from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine


class CoffeeMachine:
    """ Models a complete coffee machine"""

    def __init__(self):
        self.menu = Menu()
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()
        self.is_on = True

    def report(self):
        """Creates a report of all resources in the Coffee Machine"""
        self.coffee_maker.report()
        self.money_machine.report()

    def turn_off(self):
        """Turns the Coffee Machine off"""
        self.is_on = False

    def prepare_drink(self, drink_name):
        """Prepares the drink defined by drink_name"""
        drink = self.menu.find_drink(drink_name)
        if drink is None:
            return
        elif self.coffee_maker.is_resource_sufficient(drink):
            if self.money_machine.make_payment(drink.cost):
                self.coffee_maker.make_coffee(drink)

    def run(self):
        """Runs the Coffee Machine"""
        while self.is_on:
            drink_name = input(f"What would you like ({self.menu.get_items()})? ").lower()
            if drink_name == 'off':
                self.turn_off()
            elif drink_name == 'report':
                self.report()
            else:
                self.prepare_drink(drink_name)
