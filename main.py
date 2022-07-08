"""Use to solve problem posed at
    https://tarkalabs.notion.site/
        Build-a-spaceship-4f3109970436468d9ecb6c983aaa75d8
"""
from person import Person
from market import Market
from marketplace import Marketplace

def main():
    """
    Used to execute step-by-step process of finding optimal price for
    spaceship
    """

    # You are an up-and-coming intergalactic trader.

    luke = Person(name="Luke")
    print(f"Hi, I'm {luke.name}.\n")

    # You want to start building your fleet of logistic vessels.
    # some solar systems are not entirely friendly, your ship needs to
    # have defense capabilities as well.

    print("I want to build a spaceship. ", end="")
    print("A majestic spaceship with:")

    # A functioning ship needs the following:
    # - Engine
    # - Fuselage
    # - 20 units of Ammo
    # - Weapons system
    # - Navigation system
    # - 5 units of shields

    components_and_num_required = {"engine": 1,
                                        "fuselage": 1,
                                        "ammo": 20,
                                        "weaponsSystem": 1,
                                        "navigationSystem": 1,
                                        "shield": 5}

    for component, number_required in components_and_num_required.items():
        print(f" - {number_required} {component}")

    # Your currency portfolio looks as below:
    # CURA - 20000
    # CURB - 200
    # CURC - 5000

    luke.wallet.add_money(20000, "CURA")
    luke.wallet.add_money(200, "CURB")
    luke.wallet.add_money(5000, "CURC")

    print("\nThis will cost money. ", end="")
    print("But I have money. ", end="")
    print("Look at all of my money:\n")

    for currency, amount in luke.wallet.currencies_and_amounts:
        print(f" {amount} {currency}")

    print()
    # Market A - accepts currency A - It then offers goods and services denominated in Currency A.
    # shields - 20 CURA
    # ammo - 4 CURA
    # 1 CURB - 50 CURA

    market_a = Market("A", "CURA")
    market_a.add_product("shield", 20)
    market_a.add_product("ammo", 4)
    market_a.add_exchange_rate("CURB", 50)

    # Market B - accepts Currency B
    # shields - 20 CURB
    # ammo - 4 CURB
    # Engine - 20 CURB
    # Ship Fuselage  - 5 CURB
    # Weapon system - 10 CURB
    # CURC - 0.8 CURB
    # CURA - 0.025 CURB

    market_b = Market("B", "CURB")
    market_b.add_product("shield", 20)
    market_b.add_product("ammo", 4)
    market_b.add_product("engine", 20)
    market_b.add_product("fuselage", 5)
    market_b.add_product("weaponsSystem", 10)
    market_b.add_exchange_rate("CURC", 0.8)
    market_b.add_exchange_rate("CURA", 0.025)

    # Market C accepts Currency C
    # Shields - 20 CURC
    # Engine - 25 CURC
    # Ammo - 8 CURC
    # Navigation System - 5 CURC
    # Weapon system - 20 CURC
    # CURB - 1.2 CURC
    market_c = Market("C", "CURC")
    market_c.add_product("shield", 20)
    market_c.add_product("engine", 25)
    market_c.add_product("ammo", 8)
    market_c.add_product("navigationSystem", 5)
    market_c.add_product("weaponsSystem", 20)
    market_c.add_exchange_rate("CURB", 1.2)

    # For ease of use, we're going to add all our markets into a Marketplace

    marketplace = \
        Marketplace([market_a, market_b, market_c])

    # Assuming the costs for shipping and assembly are zero, figure out the
    # # most optimal strategy to build a ship. Good luck!  You will be graded
    # on how modular and readable the code is. Bonus points for making the
    # solution unit testable.

    # For each component in the ship:
    for ship_component, number_required in \
            components_and_num_required.items():
        # Find the Market with the best price:
        market_with_lowest_price = \
            marketplace.market_with_lowest_price(ship_component)

        print(f'The {ship_component} is cheapest in market '
              f'{market_with_lowest_price.name}, with a price of '
              f'{market_with_lowest_price.price(ship_component)} '
              f'{market_with_lowest_price.currency}.')

        # Find the price of the component in that Market
        price_of_component = market_with_lowest_price.price(ship_component)

        # Determine if I have enough of the given currency to purchase the
        # number off ship components required:
        total_cost = price_of_component * number_required

        if luke.wallet.amount_of_currency(market_with_lowest_price.currency) \
                >= total_cost:
            luke.buy(ship_component, number_required, market_with_lowest_price)

        amount_remaining = \
            luke.wallet.amount_of_currency(market_with_lowest_price.currency)

        print(f"After purchasing {number_required} {ship_component}, I have "
              f"{amount_remaining} {market_with_lowest_price.currency} "
              f"left.\n")

    print("And just to prove I bought it all, look at my possessions!\n")
    for possession, number in luke.possessions_and_number:
        print(f"{number} {possession}")

    for receipt in luke.all_receipts:
        print(luke.receipt.toJson())

    # print("\nThis will cost money. ", end="")
    # print("But I have money. ", end="")
    # print("Look at all of my money:\n")
    #
    # for currency, amount in luke.wallet.currencies_and_amounts:
    #     print(f" {amount} {currency}")

    print("\nSo let's build a spaceship!\n")

    # Buckle your seatbelts. This is where it happens.
    # You don't just buy a spaceship at your friendly
    # neighborhood NASA dealership. You build your own.
    luke.build_spaceship(components_and_num_required, "super_awesome_ship_3000")

    print("And now, I present to you my prized possession!\n")

    for possession, number in luke.possessions_and_number:
        print(f"{number} {possession}")

if __name__ == "__main__":
    main()
