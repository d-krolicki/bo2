from structure import *
from random import randint
from copy import deepcopy
"""
Wydaje mi sie, ze powinno przyjmowac argument po prostu obiekt typu Shop, a zwracac obiekt typu Solution.
"""
def algo(shop: Shop) -> Solution:
    pass


def stop_cond():
    #warunki stopu alogrytmu 
    pass


if __name__=="__main__":
    Car('VW' , 50)
    Car('Ford', 40)
    nasz_sklep = Shop()
    with open('Produkty.txt', 'r', encoding='utf8') as f:
        for lines in f.readlines():
            nasz_sklep.add_product(Product(lines, 0), randint(1,30))  
    with open('Hurtownie.txt', 'r', encoding='utf8') as f:
        for lines in f.readlines():
            nasz_sklep.add_wholesaler(Wholesaler(randint(1,40)))
    for wholesaler in nasz_sklep.wholesalers:
        for prod in nasz_sklep.w_pi:
            wholesaler.add_product(Product(prod, randint(1,15)), randint(0,100))

    pass
