from time import sleep
from wallet import Wallet
import json

class Person:
    """
    Represents a person with a name, a wallet, and things that the person
    owns. Implemented with ability to hold multiple
    user-defined currencies.
    """

    def __init__(self, name):

        self.name = name
        self.wallet = Wallet()

        # Log of what person owns as well as number thereof
        self.__possessions_and_number = {}

        self.receipts = []

    @property
    def possessions_and_number(self):
        return self.__possessions_and_number.items()

    @property
    def all_receipts(self):
        return self.receipts

    def buy(self, product, number_to_buy, market):
        """
        Purchases a specific number of a specific product in a specific market.
        """

        market.sell(self, product, number_to_buy)

    def add_product_to_possessions(self, product, number):
        if product in self.__possessions_and_number.keys():
            self.__possessions_and_number[product] += number
        else:
            self.__possessions_and_number[product] = number

    def remove_product_from_possessions(self, product, number):
        self.__possessions_and_number[product] -= number

        if self.__possessions_and_number[product] == 0:
            self.__possessions_and_number.pop(product)

    # Come back to this
    def build_spaceship(self, components_and_num_required, ship_name):
        """
        Remove elements in spaceship from person's possession, and
        replace them with a spaceship.
        """

        for component, number_required in components_and_num_required.items():
            self.remove_product_from_possessions(component, number_required)
        #     sleep(0.7)
        #
        # sleep(0.5)
        # print("Finding my tools...")
        #
        # sleep(0.5)
        # print("Moving the engine into place...")
        # self.remove_product_from_possessions("engine", 1)
        #
        # sleep(0.5)
        # print("Polishing the fuselage...")
        # self.remove_product_from_possessions("fuselage", 1)
        #
        # sleep(0.5)
        # print("Loading the ammo...")
        # self.remove_product_from_possessions("ammo", 20)
        #
        # sleep(0.5)
        # print("Adding the weapon system...")
        # self.remove_product_from_possessions("weaponsSystem", 1)
        #
        # sleep(0.5)
        # print("Adding the navigation system...")
        # self.remove_product_from_possessions("navigationSystem", 1)
        #
        # sleep(0.5)
        # print("Putting shields in place...", end="")
        # self.remove_product_from_possessions("shield", 5)
        #
        # print("Anyhow, here it is!")
        #
        # for i in range(5, 0, -1):
        #     sleep(i / 10)
        #     print("{0} ".format(i), end="")

        self.add_product_to_possessions(ship_name, 1)

