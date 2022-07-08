class Marketplace:
    """A marketplace is simply a container for a number of markets."""

    def __init__(self, markets: list):
        self.__markets = markets

    @property
    def currencies(self):
        """Returns all currencies used across all markets"""
        all_currencies = []
        for market in self.__markets:
            if market.currency not in all_currencies:
                all_currencies.append(market.currency)
        return all_currencies

    @property
    def exchange_rates(self):
        """Returns all exchange rates across all markets"""

        convert_from_to_divide_by = {}

        # For each market, record exchange rates on record:
        for market in self.__markets:

            # We are converting from the currency of the market
            # to the currency found in other markets in the marketplace.

            market_currency = market.currency
            convert_from_to_divide_by[market_currency] = {}

            for currency, rate in market.exchange_rates:
                convert_from_to_divide_by[market_currency][currency] = \
                    rate

        # We now have all exchange rates in memory. What we want to do now
        # is determine if there is a method to convert from a given currency
        # A to currency C by first converting from A to B, then B to C.

        for from_currency in self.currencies:

            for to_currency in [x for x in self.currencies
                                if x != from_currency]:

                # If we do not have a way to convert from the given currency
                # to this currency, attempt to find one:
                if to_currency not in \
                        convert_from_to_divide_by[from_currency].keys():
                    other_currencies = [x for x in self.currencies
                                        if x not in
                                        (from_currency, to_currency)]

                    for other_currency in other_currencies:

                        # If we already have an exchange rate from the
                        # starting currency to this currency, and an
                        # exchange rate from this currency to the end
                        # currency, we can convert from the starting
                        # currency to the ending currency

                        if convert_from_to_divide_by[from_currency][
                            other_currency] is not None and \
                                convert_from_to_divide_by[other_currency][
                                    to_currency] is not None:
                            convert_from_to_divide_by[from_currency][
                                to_currency] = \
                                convert_from_to_divide_by[from_currency][
                                    other_currency] * \
                                convert_from_to_divide_by[other_currency][
                                    to_currency]

        return convert_from_to_divide_by

    def market_with_lowest_price(self, product_to_check: str):
        """Finds lowest price on product in all markets in marketplace"""

        # Convert the price of the product to one standard
        # currency, compare them, and return the market with the lowest price.

        standard_currency = self.currencies[0]

        lowest_price = None
        market_with_lowest_price = None

        for market in self.__markets:

            if product_to_check in market.products:

                if market.currency == standard_currency:

                    price_in_standard_currency = market.price(product_to_check)

                else:

                    price_in_standard_currency = \
                        market.price(product_to_check) / \
                        self.exchange_rates[market.currency][standard_currency]

                if lowest_price is None:

                    lowest_price = price_in_standard_currency
                    market_with_lowest_price = market

                elif price_in_standard_currency < lowest_price:

                    lowest_price = price_in_standard_currency
                    market_with_lowest_price = market

        return market_with_lowest_price
