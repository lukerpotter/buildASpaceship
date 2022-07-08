import unittest
from market import Market
from person import Person


class TestMarket(unittest.TestCase):

    def setUp(self):
        self.person = Person(name="testPerson")
        self.person.wallet.add_money(8, "CAD")
        self.person.add_product_to_possessions("snowball", 2)

    def test_possessions_and_number(self):
        self.assertEqual(self.person.possessions_and_number,
                         {"snowball": 2}.items())

    def test_buy(self):
        self.market = Market("Canada", "CAD")
        self.market.add_product("waffle", 4)

        self.person.buy("waffle", 2, self.market)

        # Ensure person received possession

        possessions_and_number = {"snowball": 2, "waffle": 2}
        self.assertEqual(self.person.possessions_and_number,
                         possessions_and_number.items())

        # Ensure money was removed from persons' wallet:

        self.assertEqual(self.person.wallet.amount_of_currency("CAD"), 0)

        # Ensure money was added to market's wallet (2 waffles @ 4 CAD)

        self.assertEqual(self.market.wallet.amount_of_currency("CAD"), 8)

    def test_add_product_to_possessions(self):
        self.person.add_product_to_possessions("snowmen", 42)
        possessions_and_number = {"snowball": 2, "snowmen": 42}
        self.assertEqual(self.person.possessions_and_number,
                         possessions_and_number.items())

    def test_remove_product_from_possessions(self):
        self.person.remove_product_from_possessions("snowball", 1)
        possessions_and_number = {"snowball": 1}
        self.assertEqual(self.person.possessions_and_number,
                         possessions_and_number.items())