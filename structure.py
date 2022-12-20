import numpy as np
from random import *
from typing import List, Tuple

seed(10)


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
    def __init__(self, name: str, id_h: int) -> None:
        self.id = id_h
        self.name = name
        self.products = {}

    def add_product_for_wholesaler(self, product: Product, amount: int) -> None:
        self.products[product] = [product.id, product.price, amount]  # tutaj jest haczyk - kluczem w slowniku musi byc obiekt klasy Product, a nie sama jego nazwa



class Shop:
    def __init__(self) -> None:
        self.max_id_hurt = 0
        self.max_id_prod = 0
        self.wholesalers = []
        self.distances = np.array([[]])
        self.products = {}
        self.cars = []  # samochody z określoną pojemnością

    def add_wholesaler(self, wholesaler: Wholesaler) -> None:
        self.wholesalers.append(wholesaler)
        self.max_id_hurt += 1

    def add_product_for_shop(self, product: Product, demand: int) -> None:
        self.products[
            product] = demand  # tutaj jest haczyk - kluczem w slowniku musi byc obiekt klasy Product, a nie sama jego nazwa
        self.max_id_prod += 1
    def add_car(self, car: Car):
        self.cars.append(car)


class Solution:
    def __init__(self) -> None:
        self.m_sol = np.array([])  # macierz ilości produktów pobieranych z konkretnej hurtowni n x i
        self.iteration = 0  # liczba wykonanych iteracji


# wydaje mi się, że potrzebujemy klase osobnik w ktorej będzie wszystko tym jaka jest wartośc funcji celu dla danego osobnika,
# mutacje w nim , crossover czyli jak powstje następny z dwóch rodziców, i struktóra mówiąca o tym jakie produkty bierzemy z danegj hurtowni
# do tego stworzymy klase population która będzie przechowywać rozmiar populacji tworzenie początkowej, i generalnie wszystkich osobników danej populacji
# nie mam pojęcia w jakiej strukturze przechowywać dane o osobniku
class Sample:
    def __init__(self, solution: List[List[List[Tuple]]]) -> None:
        self.cost = np.inf
        self.solution = solution

    # def __str__(self):
    #     ret = ""


    def mutation(self):
        # mutacje
        pass

    def objective_function(sol: Solution, shop: Shop):
        # funkcja kosztu
        pass


class Population:
    def __init__(self, population_size) -> None:
        population = []
        self.population_size = population_size

    def initial_sample(self, shop: Shop):
        '''
        Tworzy pojedyńczego osobnika początkowego
        '''
        n_cars = len(shop.cars)
        solution = []
        for car in range(n_cars):   # iteracja po ID samochodów
            solution.append([])
            path = choices(shop.wholesalers, k=randint(0, 2*len(shop.wholesalers)))
            for w in path:# iteracja po ID hurtowni
                solution[car].append(len(path)*[])
                for product in w.products:
                    print(f"w.id:{w.id}")
                    solution[car][w.id].append((product, randint(0, np.round(213.7))))
        return Sample(solution=solution)

    def crossover(self, parent1, parent2):
        # krzyżowanie osobników
        pass

    def initial_population(self):
        pass
