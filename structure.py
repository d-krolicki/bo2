class Car:
    def __init__(self, name, capacity) -> None:
        self.name = name
        self.capacity = capacity


class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class Wholesaler:
    def __init__(self, distance: int) -> None:
        self.dist_hurt = distance
        self.trans_price = 2 * distance
        self.prod_list = {}

    def add_product(self, product: Product, ilosc, price) -> None:
        self.prod_list[product.name] = [product.price, ilosc]


class Shop:
    def __init__(self) -> None:
        self.wholesalers = []
        self.w_pi = {}
        self.cars = []  # samochody z określoną pojemnością

    def add_wholesaler(self, wholesaler: Wholesaler):
        self.wholesalers.append(wholesaler)

    def add_product(self, product, demand):
        self.w_pi[product.name] = demand


class Solution:
    def __init__(self) -> None:
        self.m_sol = [[]]  # macierz ilości produktów pobieranych z konkretnej hurtowni n x i
        self.iteration = 0  # liczba wykonanych iteracji
