import random

from algorithm import *
from structure import *
from utils import print_summary

# stworzenie pustej struktury danych - sklepu
nasz_sklep = Shop()

# dodawanie produktów
with open('Produkty.txt', 'r', encoding='utf8') as f:
    prodMat = []
    for lines in f.readlines():
        lines = lines.split()
        if lines:
            prodMat.append([val.replace("_", " ") if count == 0 else int(val) for count, val in enumerate(lines)])
    for product in prodMat:
        nasz_sklep.add_product_for_shop(Product(name=product[0], price=product[1], id_p=nasz_sklep.max_id_prod), randint(1, 30))

# dodawanie macierzy odległości
with open('distances.txt', 'r', encoding='utf8') as f:
    distMat = []  # distances matrix
    for line in f.readlines():
        line = line.split()
        if line:
            distMat.append([int(i) for i in line])

# dodawanie samochodów
with open('cars.txt', 'r', encoding='utf8') as f:
    carMat = []
    for line in f.readlines():
        line = line.split()
        if line:
            carMat.append([val if count == 0 else int(val) for count, val in enumerate(line)])
    for c in carMat:
        nasz_sklep.add_car(Car(c[0], c[1]))

# dodawanie hurtowni
with open('Hurtownie.txt', 'r', encoding='utf8') as f:
    for count, lines in enumerate(f.readlines()):
        nasz_sklep.add_wholesaler(Wholesaler(lines[:-1], nasz_sklep.max_id_hurt, distMat[count]))

# dodawanie produktów do hurtowni
for wholesaler in nasz_sklep.wholesalers:
    for prod in nasz_sklep.products:
        wholesaler.add_product_for_wholesaler(prod, randint(0, 100))

# ustalanie cen w hurtowniach

if __name__ == "__main__":
    # pogląd danych
    # print_summary(nasz_sklep)

    test = Population(nasz_sklep, 1)
    iniSample1 = test.initial_sample()
    iniSample2 = test.initial_sample()
    print(iniSample1)
    print(iniSample2)
    print(test.crossover(iniSample1, iniSample2)[0])
    print(test.crossover(iniSample1, iniSample2)[1])
    
    # print(iniSample)
    # for _ in range(10000):
    #     iniSample.mutation(True, False, False)
    # print(iniSample)

    # for wholesaler in iniSample.shop.wholesalers:
    #    for product in nasz_sklep.products:
    #        print(f"{product.name} : {wholesaler.products[product][0]}, {wholesaler.products[product][1]}, {wholesaler.products[product][2]}")
    #    print()

    # print(iniSample)
    # for w in iniSample.shop.wholesalers:
    #    print(w.distances)
    # print(round(iniSample.objective_function(), 3))
