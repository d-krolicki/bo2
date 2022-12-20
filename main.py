from algorithm import *
from structure import *
from utils import print_summary

# stworzenie pustej struktury danych - sklepu
nasz_sklep = Shop()

# dodawanie produktów
with open('Produkty.txt', 'r', encoding='utf8') as f:
    for lines in f.readlines():
        nasz_sklep.add_product_for_shop(Product(lines[:-1], 0, nasz_sklep.max_id_prod), randint(1,30))

# dodawanie hurtowni
with open('Hurtownie.txt', 'r', encoding='utf8') as f:
    for lines in f.readlines():
        nasz_sklep.add_wholesaler(Wholesaler(lines[:-1], nasz_sklep.max_id_hurt))

# dodawanie produktów do hurtowni
for wholesaler in nasz_sklep.wholesalers:
    for prod in nasz_sklep.products:
        wholesaler.add_product_for_wholesaler(prod, randint(0, 100))

nasz_sklep.add_car(Car("volvo", 50))

# pogląd danych
# print_summary(nasz_sklep)


test = Population(1)
iniSample = test.initial_sample(nasz_sklep)
print(iniSample.solution)


