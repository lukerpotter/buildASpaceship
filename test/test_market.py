import unittest
from market import Market
from person import Person


class TestMarket(unittest.TestCase):

    def setUp(self):
        self.market = Market("Canada", "CAD")
        self.market.add_exchange_rate("USD", 0.83)
        self.market.add_product("poutine", 20)
        self.market.add_product("hockey_puck", 4)

        self.products_and_prices = {"poutine": 20, "hockey_puck": 4}

    def test_currency(self):
        self.assertEqual(self.market.currency, "CAD")

    def test_exchange_rates(self):
        self.assertEqual(self.market.exchange_rates, ({"USD": 0.83}).items())

    def test_products_and_prices(self):
        self.assertEqual(self.market.products_and_prices,
                         self.products_and_prices.items())

    def test_products(self):
        self.assertEqual(self.market.products,
                         self.products_and_prices.keys())

    def test_add_exchange_rate(self):
        self.market.add_exchange_rate("BRX", 1.25)
        self.assertEqual(self.market.exchange_rates,
                         ({"USD": 0.83, "BRX": 1.25}).items())

    def test_add_product(self):
        self.market.add_product("timbit", 0.25)
        self.assertEqual(self.market.products_and_prices,
                         ({"poutine": 20,
                           "hockey_puck": 4,
                           "timbit": 0.25}).items())

    def test_price(self):
        self.assertEqual(self.market.price("hockey_puck"), 4)

    def test_sell(self):
        test_person = Person("person")
        test_person.wallet.add_money(4, "CAD")
        self.market.sell(test_person, "hockey_puck", 1)

        # Ensure person received possession

        possessions_and_number = {"hockey_puck": 1}
        self.assertEqual(test_person.possessions_and_number,
                         possessions_and_number.items())

        # Ensure money was removed from persons' wallet:

        self.assertEqual(test_person.wallet.amount_of_currency("CAD"), 0)

        # Ensure money was added to market's wallet

        self.assertEqual(self.market.wallet.amount_of_currency("CAD"), 4)