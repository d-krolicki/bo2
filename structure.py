import numpy as np
from random import *
from typing import List, Tuple
from copy import copy


# seed(10)


class Car:
    def __init__(self, name: str, capacity: int) -> None:
        self.name = name
        self.capacity = capacity


class Product:
    def __init__(self, name: str, price: int, id_p: int) -> None:
        self.id = id_p
        self.name = name
        self.price = price


class Wholesaler:
    def __init__(self, name: str, id_h: int, dist: List) -> None:
        self.id = id_h
        self.name = name
        self.products = {}
        self.distances = dist

    def add_product_for_wholesaler(self, product: Product, amount: int) -> None:
        self.products[product] = [product.id, product.price, amount]


class Shop:
    def __init__(self) -> None:
        self.max_id_hurt = 0
        self.max_id_prod = 0
        self.wholesalers = []
        self.products = {}
        self.cars = []  # samochody z określoną pojemnością

    def add_wholesaler(self, wholesaler: Wholesaler) -> None:
        self.wholesalers.append(wholesaler)
        self.max_id_hurt += 1

    def add_product_for_shop(self, product: Product, demand: int) -> None:
        self.products[product] = demand  # tutaj jest haczyk - kluczem w slowniku musi byc obiekt klasy Product, a nie sama jego nazwa
        self.max_id_prod += 1

    def add_car(self, car: Car):
        self.cars.append(car)


class Solution:
    def __init__(self) -> None:
        self.m_sol = np.array([])  # macierz ilości produktów pobieranych z konkretnej hurtowni n x i
        self.iteration = 0  # liczba wykonanych iteracji


# wydaje mi się, że potrzebujemy klase osobnik w ktorej będzie wszystko tym jaka jest wartośc funcji celu dla danego
# osobnika, mutacje w nim , crossover czyli jak powstje następny z dwóch rodziców, i struktóra mówiąca o tym jakie
# produkty bierzemy z danegj hurtowni do tego stworzymy klase population która będzie przechowywać rozmiar populacji
# tworzenie początkowej, i generalnie wszystkich osobników danej populacji nie mam pojęcia w jakiej strukturze
# przechowywać dane o osobniku
class Sample:
    def __init__(self, shop: Shop, solution: List[List[List[Tuple]]], paths) -> None:
        self.shop = shop
        self.cost = np.inf
        self.solution = solution
        self.paths = paths  # drogi dla każdego z samochodów (lista zawierająca ID hurtowni w kolejności odwiedzania)

    def __str__(self):  # UWAGA działa tylko gdy liczba produktów we wszystkich hurtowniach jest taka sama
        sol = '====================================\n'
        for c, car in enumerate(self.solution):  # iteracja po samochodach
            sol += f'Samochód {c + 1}\n\n'
            sol += '{:20}'.format('Produkt \ Hurtownia')
            for w in self.paths[c]:  # iteracja po drogach (wypisanie indeksów hurtowni)
                sol += f'{w.id: 4} '
            sol += '\n'
            for p in range(len(self.solution[c][0])):  # iteracja po produktach (kolumnach)
                sol += f'{self.solution[c][0][p][0].name:20} '
                for h in range(len(self.paths[c])):  # iteracja po hurtowniach (wierszach)
                    sol += f'{self.solution[c][h][p][1]:3}  '
                sol += '\n'
            sol += '====================================\n'
        return sol

    def mutation(self, random_change_value: bool, random_swap: bool, add_or_sub_stop:bool):
        '''
        Mutacje 
        Mamy trzy możliwości mutacji:
        - w losowym miejsciu zmieniamy warość zakupów 
        - wymieniamy ze sobą kolejność odwiedzania
        - dodajemy/odejmujemy odwiedzane miejsce 
        '''
        if random_change_value:
            car = randint(0, len(self.solution)-1)
            stop_place = randint(0, len(self.solution[car])-1)
            product = randint(0,len(self.solution[car][stop_place])-1)
            val = randint(0, int(213.7))
            self.solution[car][stop_place][product] = self.solution[car][stop_place][product][0],val
        elif random_swap:
            car = randint(0, len(self.solution)-1)
            stop_place_to_swap_1 = randint(0, len(self.solution[car])-1)
            stop_place_to_swap_2 = randint(0, len(self.solution[car])-1)
            self.solution[car][stop_place_to_swap_1], self.solution[car][stop_place_to_swap_2] = self.solution[car][stop_place_to_swap_2], self.solution[car][stop_place_to_swap_1]
            self.paths[car][stop_place_to_swap_1], self.paths[car][stop_place_to_swap_2] = self.paths[car][stop_place_to_swap_2], self.paths[car][stop_place_to_swap_1]
        elif add_or_sub_stop:
            add_or_sub = randint(0,1)
            car = randint(0, len(self.solution)-1)
            stop_place = randint(0, len(self.solution[car]))
            if add_or_sub:
                wholesaler = choices(self.shop.wholesalers, k=1)[0]
                self.solution[car].insert(stop_place, [])
                for product in wholesaler.products:
                    self.solution[car][stop_place].append((product, randint(0, np.round(213.7))))
                self.paths[car].insert(stop_place, wholesaler) 
            else:
                if len(self.solution[car])> 1:
                    stop_place = randint(0, len(self.solution[car])-1)
                    del self.solution[car][stop_place]
                    del self.paths[car][stop_place]
        return self.solution


    def objective_function(self):
        # @FIXME: teraz dystanse dodawane są z pliku txt i trzeba poprawić odczytywanie dystansu
        self.cost = np.inf
        print("========================================================================")
        print("Starting delivery.")
        for j, car in enumerate(self.solution):
            print(
                f"Car {j + 1} starts by visiting wholesaler {self.paths[j][0].id}, cost equals {self.paths[j][0].distances[-1]}.")
            self.cost += self.paths[j][0].distances[-1]
            for i, shopping_list in enumerate(car):
                # print(shopping_list)
                for tup in shopping_list:
                    # pass
                    self.cost += tup[1] * self.paths[j][i].products[tup[0]][1]
                try:
                    print(
                        f"Car {j + 1} is driving from wholesaler {self.paths[j][i].id} to wholesaler {self.paths[j][i + 1].id}, cost equals {self.paths[j][i].distances[self.paths[j][i + 1].id]}.")
                    self.cost += self.paths[j][i].distances[self.paths[j][i + 1].id]
                except:
                    print(
                        f"Car {j + 1} driving from wholesaler {self.paths[j][i].id} to shop, cost is {self.paths[j][i].distances[-1]}.")
                    self.cost += self.paths[j][i].distances[-1]

        print("Ending delivery.")
        print("========================================================================")
        return self.cost


class Population:
    def __init__(self, shop: Shop, population_size) -> None:
        self.shop = shop
        self.population = []
        self.population_size = population_size
        self.generation_counter = 1

    def initial_sample(self):
        """
        Tworzy pojedyńczego osobnika początkowego
        """
        n_cars = len(self.shop.cars)
        solution = []
        paths = []
        for car in range(n_cars):  # iteracja po ID samochodów
            solution.append([])
            path = choices(self.shop.wholesalers, k=randint(1, 2 * len(self.shop.wholesalers)))
            paths.append(path)
            for _ in range(len(path)):
                solution[car].append([])
            i = 0
            for w in path:  # iteracja po ID hurtowni
                for product in w.products:
                    solution[car][i].append((product, randint(0, np.round(213.7))))
                i += 1
        return Sample(self.shop, solution=solution, paths=paths)

    def crossover(self, parent1, parent2):
        '''
        Krzyżownaie 
        Z dwóch rodziców losowo wybieramy miejsce krzyżówki genów. 
        Powstanie dwójka dzieci
        Zasada działania
        rodzice:
        11111111
        00000000
        dzieci:
        11100000
        00011111
        ''' 
        child1 = []
        child2 = []
        path_child1 = []
        path_child2 = []
        for car in range(len(parent1.solution)):
            child1.append([]), child2.append([]),path_child1.append([]), path_child2.append([])
            cross_place = randint(0, min(len(parent1.solution[car]), len(parent2.solution[car])))
            for _ in range(len(parent1.solution[car])): child1[car].append([]),path_child1[car].append([])
            for _ in range(len(parent2.solution[car])): child2[car].append([]),path_child2[car].append([]) 

            for i in range(len(parent1.solution[car])):
                if i <= cross_place and i < len(parent2.solution[car]):
                    child1[car][i] = parent2.solution[car][i]
                    path_child1[car][i] = parent2.paths[car][i]
                else:
                    child1[car][i] = parent1.solution[car][i] 
                    path_child1[car][i] = parent1.paths[car][i] 
            for i in range(len(parent2.solution[car])):
                if i <= cross_place and i < len(parent1.solution[car]):
                    child2[car][i] = parent1.solution[car][i]
                    path_child2[car][i] = parent1.paths[car][i]
                else:
                    child2[car][i] = parent2.solution[car][i] 
                    path_child2[car][i] = parent2.paths[car][i]
        child1 = Sample(self.shop, child1, path_child1)
        child2 = Sample(self.shop, child2, path_child2)
        return child1, child2

    def initial_population(self):
        for size in range(self.population_size):
            self.population.append(self.initial_sample(self.shop))
