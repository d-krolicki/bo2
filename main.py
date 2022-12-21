import random

from algorithm import *
from structure import *
from utils import print_summary

# stworzenie pustej struktury danych - sklepu
nasz_sklep = Shop()

# dodawanie produktów
with open('Produkty.txt', 'r', encoding='utf8') as f:
    for lines in f.readlines():
        nasz_sklep.add_product_for_shop(Product(name=lines[:-1], price=1, id_p=nasz_sklep.max_id_prod), randint(1, 30))

# dodawanie hurtowni
with open('Hurtownie.txt', 'r', encoding='utf8') as f:
    x = f.readlines()
    for lines in x:
        lst = [randint(100, 222) for _ in range(len(x)+1)]
        lst[nasz_sklep.max_id_hurt] = 0
        nasz_sklep.add_wholesaler(Wholesaler(lines[:-1], nasz_sklep.max_id_hurt, lst))

# dodawanie produktów do hurtowni
for wholesaler in nasz_sklep.wholesalers:
    for prod in nasz_sklep.products:
        wholesaler.add_product_for_wholesaler(prod, randint(0, 100))

nasz_sklep.add_car(Car("volvo", 50))
nasz_sklep.add_car(Car('honda', 30))

# pogląd danych
# print_summary(nasz_sklep)


if __name__ == "__main__":
    test = Population(shop=nasz_sklep, population_size=1)
    iniSample = test.initial_sample(nasz_sklep)
    print(iniSample)
    for w in nasz_sklep.wholesalers:
        print(w.distances)
    print()
    print(iniSample.objective_function())

