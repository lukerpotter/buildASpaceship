import unittest
from wallet import Wallet


class TestMarket(unittest.TestCase):

    def setUp(self):
        self.wallet = Wallet()
        self.wallet.add_money(10, "USD")

    def test_currencies(self):
        self.assertEqual(self.wallet.currencies, {"USD": 0}.keys())

    def test_currencies_and_amounts(self):
        self.assertEqual(self.wallet.currencies_and_amounts,
                         {"USD": 10}.items())

    def test_amount_of_currency(self):
        self.assertEqual(self.wallet.amount_of_currency("USD"), 10)

    # Because currencies are stored in a dictionary, and we can't add or
    # remove values from a dictionary if the key is not already present,
    # we have to check if the key exists first.

    def test_add_money(self):
        self.wallet.add_money(1, "USD")
        self.assertEqual(self.wallet.amount_of_currency("USD"), 11)

    def remove_money(self):
        self.wallet.remove_money(1, "USD")
        self.assertEqual(self.wallet.amount_of_currency("USD"), 1)

    def test_transfer_money_to_other_wallet(self):
        test_wallet = Wallet()
        self.wallet.transfer_money_to_other_wallet(6, "USD", test_wallet)

        # Assert that money has been removed from our wallet

        self.assertEqual(self.wallet.amount_of_currency("USD"), 4)

        # Assert that money has been added to test wallet

        self.assertEqual(test_wallet.amount_of_currency("USD"), 6)