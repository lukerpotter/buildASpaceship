from person import Person
from wallet import Wallet

class Market:
    '''
    Represents a Market that trades in a specific currency, and can also
    exchange that currency for others to be used in other markets.
    '''

    def __init__(self, name: str, currency: str):
        self.__name = name
        self.__currency = currency
        self.__currenciesAndExchangeRates = {}
        self.__availableProductsAndPrices = {}

        self.__wallet = Wallet()
        self.__wallet.add_money(currency, 0)

    @property
    def name(self):
        return self.__name

    @property
    def currency(self):
        return self.__currency

    @property
    def exchange_rates(self):
        return self.__currenciesAndExchangeRates.items()

    @property
    def products_and_prices(self):
        return self.__availableProductsAndPrices.items()

    @property
    def products(self):
        return self.__availableProductsAndPrices.keys()

    @property
    def wallet(self):
        return self.__wallet

    def add_exchange_rate(self, currency: str, rate: float):
        self.__currenciesAndExchangeRates[currency] = rate

    def add_product(self, product: str, price: float):
        self.__availableProductsAndPrices[product] = price

    def price(self, product: str):
        return self.__availableProductsAndPrices[product]

    def sell(self, buyer: Person, product: str, number_to_buy: int):
        """Sell an item to the buyer by transferring money from the buyer's
        wallet to our wallet and adding the item to his/her possessions."""

        buyer.wallet.transfer_money_to_other_wallet(self.price(product) *
                                                    number_to_buy,
                                                    self.currency,
                                                    self.__wallet)

        buyer.add_product_to_possessions(product, number_to_buy)
