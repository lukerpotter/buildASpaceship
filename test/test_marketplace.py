import unittest
from market import Market
from marketplace import Marketplace


class TestMarketplace(unittest.TestCase):

    def setUp(self):
        self.market_a = Market("A", "CURA")
        self.market_a.add_product("test_product", 20)
        self.market_a.add_exchange_rate("CURB", 2)

        self.market_b = Market("B", "CURB")
        self.market_b.add_product("test_product", 20)
        self.market_b.add_exchange_rate("CURA", 1.2)
        self.market_b.add_exchange_rate("CURC", 2)

        self.market_c = Market("C", "CURC")
        self.market_c.add_product("test_product", 20)
        self.market_c.add_exchange_rate("CURB", 0.6)

        self.marketplace = \
            Marketplace([self.market_a, self.market_b, self.market_c])

    def test_currencies(self):
        self.assertEqual(self.marketplace.currencies, ['CURA', 'CURB', 'CURC'])

    def test_exchange_rates(self):
        # Expected results :
        # From  To  DivideBy
        # ----  --  --------
        # A     B      2
        # A     C      4 (A to B = divide by 2; B to C = divide by 2)
        # B     A      1.2
        # B     C      2
        # C     B      0.6
        # C     A      0.72 (C to B = divide by 0.6; B to A = divide by 1.2)

        self.assertEqual(self.marketplace.exchange_rates,
                         {'CURA': {'CURB': 2, 'CURC': 4},
                          'CURB': {'CURA': 1.2, 'CURC': 2},
                          'CURC': {'CURB': 0.6, 'CURA': 0.72}})

    def test_market_with_lowest_price(self):

        # We have a test product in each of our markets with a price of 20.
        # Converting all to currency A:
        # Market A = 20
        # Market B = 16.7
        # Market C = 27.8

        self.assertEqual(
            self.marketplace.market_with_lowest_price("test_product").name,
            self.market_b.name)