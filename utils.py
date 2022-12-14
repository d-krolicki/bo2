from structure import *
from algorithm import *

"""
Prints summary of the shop's available, products, demands and available wholesalers with their offers.
"""

def print_summary(shop: Shop) -> None:
    print("----- SHOWING PRODUCTS AND DEMANDS -----" + '\n')

    for p in shop.products.keys():
        print(f"{p.name} : {shop.products[p]}")

    print()

    # print("----- SHOWING WHOLESALERS, PRICES AND STOCKS -----" + '\n')

    # for w in shop.wholesalers:
    #     print(f"{w.name}")
    #     for p in w.products.keys():
    #         print(
    #             f"{p.name} : {w.products[p][0]} for one piece, {w.products[p][1]} in stock.")
    #     print()
