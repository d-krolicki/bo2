import numpy as np

class Car:
    def __init__(self, name: str, capacity: int) -> None:
        self.name = name
        self.capacity = capacity


class Product:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price


class Wholesaler:
    def __init__(self, distance: int) -> None:
        self.dist_hurt = distance
        self.trans_price = 2 * distance
        self.prod_list = {}

    def add_product(self, product: Product, amount: int) -> None:
        self.prod_list[product.name] = [product.price, amount]


class Shop:
    def __init__(self) -> None:
        self.wholesalers = []
        self.w_pi = {}
        self.cars = []  # samochody z określoną pojemnością

    def add_wholesaler(self, wholesaler: Wholesaler) -> None:
        self.wholesalers.append(wholesaler)

    def add_product(self, product: Product, demand: int) -> None:
        self.w_pi[product.name] = demand
    
    def add_cars(self,car :Car):
        self.cars.append(car)
        
class Solution:
    def __init__(self) -> None:
        self.m_sol = [[]]  # macierz ilości produktów pobieranych z konkretnej hurtowni n x i
        self.iteration = 0  # liczba wykonanych iteracji

#wydaje mi się, że potrzebujemy klase osobnik w ktorej będzie wszystko tym jaka jest wartośc funcji celu dla danego osobnika, 
#mutacje w nim , crossover czyli jak powstje następny z dwóch rodziców, i struktóra mówiąca o tym jakie produkty bierzemy z danegj hurtowni
#do tego stworzymy klase population która będzie przechowywać rozmiar populacji tworzenie początkowej, i generalnie wszystkich osobników danej populacji
#nie mam pojęcia w jakiej strukturze przechowywać dane o osobniku 
class Osobnik:
    def __init__(self) -> None:
        cost = np.inf
        pass
    
    def crossover(self, parent1, parent2):
        #krzyżowanie osobników 
        pass

    def mutacion(self):
        #mutacje
        pass

    def objective_function(sol :Solution, shop: Shop):
        #funkcja kosztu
        pass    

class Populacja:
    def __init__(self, population_size) -> None:
        population = []
        population_size = population_size

    def initial_population(self):
        #populacja początkowa
        pass    