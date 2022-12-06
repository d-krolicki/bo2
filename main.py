class Car:
    def __init__(self, name, pojemnosc) -> None:
        self.name = name
        self.pojemnosc = pojemnosc


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


class Sklep:
    def __init__(self) -> None:
        self.hurt = []
        self.w_pi = {}
        self.cars = []  # samochody z określoną pojemnością

    def add_hurtowania(self, wholesaler: Wholesaler):
        self.hurt.append(wholesaler)

    def add_product(self, product, demand):
        self.w_pi[product.name] = demand


class Rozwiazanie:
    def __init__(self) -> None:
        self.m_sol = [[]]  # macierz ilości produktów pobieranych z konkretnej hurtowni n x i
        self.iteration = 0  # liczba wykonanych iteracji


def algo(self, m_sol):
    return None
