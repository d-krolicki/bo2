import random

from algorithm import *
from structure import *
from utils import print_summary
from gui import *


# stworzenie pustej struktury danych - sklepu
#
# nasz_sklep = Shop()
#
# # dodawanie produktów do sklepu
# with open('Data/Produkty.txt', 'r', encoding='utf8') as f:
#     prodMat = []
#     for lines in f.readlines():
#         lines = lines.split()
#         if lines:
#             prodMat.append([val.replace("_", " ") if count == 0 else int( val) for count, val in enumerate(lines)])
#     for product in prodMat:
#         nasz_sklep.add_product_for_shop(Product(name=product[0], price=product[1], id_p=nasz_sklep.max_id_prod), randint(1, 100))
#
# # dodawanie macierzy odległości
# with open('Data/distances.txt', 'r', encoding='utf8') as f:
#     distMat = []  # distances matrix
#     for line in f.readlines():
#         line = line.split()
#         if line:
#             distMat.append([int(i) for i in line])
#
# # dodawanie samochodów
# with open('Data/cars.txt', 'r', encoding='utf8 ') as f:
#     carMat = []
#     for line in f.readlines():
#         line = line.split()
#         if line:
#             carMat.append([val if count == 0 else int(val) for count, val in enumerate(line)])
#     for c in carMat:
#         nasz_sklep.add_car(Car(c[0], c[1]))
#
# # dodawanie hurtowni
# with open('Data/Hurtownie.txt', 'r', encoding='utf8') as f:
#     for count, lines in enumerate(f.readlines()):
#         nasz_sklep.add_wholesaler(Wholesaler(lines[:-1], nasz_sklep.max_id_hurt, distMat[count]))
#
# # dodawanie produktów do hurtowni
# for wholesaler in nasz_sklep.wholesalers:
#     for prod in nasz_sklep.products:
#         wholesaler.add_product_for_wholesaler(prod, randint(0, 100))

#
# if __name__ == "__main__":
#     # print(algo(nasz_sklep).cost)
#     # print(algo2(nasz_sklep)[0])
#     # print(algo2(nasz_sklep))
#
#     window = tk.Tk()
#     GUI(window)
#     window.mainloop()
