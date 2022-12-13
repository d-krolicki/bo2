from algorithm import *
from structure import *
from utils import print_summary

# stworzenie pustej struktury danych - sklepu
nasz_sklep = Shop()

# dodawanie produktów
with open('Produkty.txt', 'r', encoding='utf8') as f:
    for lines in f.readlines():
        nasz_sklep.add_product_for_shop(Product(lines[:-1], 0, nasz_sklep.max_id), randint(1,30))
        nasz_sklep.max_id += 1

# dodawanie hurtowni
with open('Hurtownie.txt', 'r', encoding='utf8') as f:
    for lines in f.readlines():
        nasz_sklep.add_wholesaler(Wholesaler(lines[:-1], randint(1, 40)))

# dodawanie produktów do hurtowni
for wholesaler in nasz_sklep.wholesalers:
    for prod in nasz_sklep.products:
        wholesaler.add_product_for_wholesaler(prod, randint(0, 100))

# pogląd danych
print_summary(nasz_sklep)

