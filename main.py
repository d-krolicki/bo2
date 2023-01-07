import random

from algorithm import *
from structure import *
from utils import print_summary
# seed(11)
# stworzenie pustej struktury danych - sklepu
nasz_sklep = Shop()

# dodawanie produktów do sklepu
with open('Data/Produkty.txt', 'r', encoding='utf8') as f:
    prodMat = []
    for lines in f.readlines():
        lines = lines.split()
        if lines:
            prodMat.append([val.replace("_", " ") if count == 0 else int(val) for count, val in enumerate(lines)])
            nasz_sklep.add_product_for_shop(Product(name=lines[0], price=int(lines[1]), id_p=nasz_sklep.max_id_prod), int(lines[1]))

# dodawanie macierzy odległości
with open('Data/distances.txt', 'r', encoding='utf8') as f:
    distMat = []  # distances matrix
    for line in f.readlines():
        line = line.split()
        if line:
            distMat.append([int(i) for i in line])

# dodawanie samochodów
with open('Data/cars.txt', 'r', encoding='utf8') as f:
    carMat = []
    for line in f.readlines():
        line = line.split()
        if line:
            carMat.append([val if count == 0 else int(val) for count, val in enumerate(line)])
    for c in carMat:
        nasz_sklep.add_car(Car(c[0], c[1]))

# dodawanie hurtowni
with open('Data/Hurtownie.txt', 'r', encoding='utf8') as f:
    for count, lines in enumerate(f.readlines()):
        nasz_sklep.add_wholesaler(Wholesaler(lines[:-1], nasz_sklep.max_id_hurt, distMat[count]))

# dodawanie produktów do hurtowni
for wholesaler in nasz_sklep.wholesalers:
    for prod in nasz_sklep.products:
        wholesaler.add_product_for_wholesaler(prod, randint(0, 100))

# ustalanie cen w hurtowniach

if __name__ == "__main__":
    for _ in range(10):
        najlepszy = algo(nasz_sklep)
        print(f'alg1 :{najlepszy.cost}', end=' ')
        najlepszy = algo2(nasz_sklep)
        print(f'alg2 :{najlepszy.cost}')
    # demand = copy.copy(nasz_sklep.products)
    # for j, car in enumerate(najlepszy.solution):
    #         for i, shopping_list in enumerate(car):
    #             for tup in shopping_list:
    #                 demand[tup[0]] -= tup[1]
    # for key , val in demand.items():
    #     # print(f'{key.name} : {nasz_sklep.products[key]} {val}')

