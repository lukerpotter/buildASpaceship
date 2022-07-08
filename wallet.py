class Wallet:
    """
    Represents a standard wallet. Implemented with ability to hold multiple
    user-defined currencies.
    """

    def __init__(self):

        # Currencies and balances are key-value pairs within the Wallet object
        # reflecting how much of a given currency is in the Wallet.
        self.__currencies_and_amounts = {}

    @property
    def currencies(self):
        """Returns all currencies currently in the wallet."""

        return self.__currencies_and_amounts.keys()

    @property
    def currencies_and_amounts(self):
        """Returns all currencies and amounts currently in the wallet."""

        return self.__currencies_and_amounts.items()

    def amount_of_currency(self, currency: str):
        """Returns amount of a given currency in the wallet."""

        return self.__currencies_and_amounts[currency]

    # Because currencies are stored in a dictionary, and we can't add or
    # remove values from a dictionary if the key is not already present,
    # we have to check if the key exists first.

    def add_money(self, amount, currency):
        """Adds a given amount of currency to the wallet."""

        if currency in self.currencies:
            self.__currencies_and_amounts[currency] += amount
        else:
            self.__currencies_and_amounts[currency] = amount

    def remove_money(self, amount, currency):
        """Removes a given amount of currency from the wallet."""

        if currency in self.currencies:
            self.__currencies_and_amounts[currency] -= amount
        else:
            self.__currencies_and_amounts[currency] = amount

    def transfer_money_to_other_wallet(self, amount, currency,
                                       wallet_receiving_money):
        """Removes money from this wallet and adds it to another wallet"""

        # I know this is a rather crude implementation, but in the context
        # of the initial problem, this had to happen somewhere, and there
        # was no real use abstracting it more. In a real-world situation,
        # this would probably be replaced with a payment API call or something
        # similar.
        self.remove_money(amount, currency)
        wallet_receiving_money.add_money(amount, currency)


