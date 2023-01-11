import numpy as np
from random import *
from typing import List, Tuple
import copy


# seed(10)


class Car:
    '''
    Class representing a car.
        Attributes
        ----------
        name : str
            Car's name.
        capacity : int
            Car's capacity.
    '''

    def __init__(self, name: str, capacity: int) -> None:
        self.name = name
        self.capacity = capacity


class Product:
    '''
    Class representing a product.
        Attributes
        ----------
        name : str
            Product's name.
        price : float
            Product's base price.
        id : int
            Product's unique ID number.
    '''

    def __init__(self, name: str, price: float, id_p: int) -> None:
        self.id = id_p
        self.name = name
        self.price = price


class Wholesaler:
    '''
    Class representing a wholesaler.
        Attributes
        ----------
        name : str
            Wholesaler's name.
        id : int
            Wholesaler's unique ID number.
        products : Dict[Product : List[int, float, int]]
            Dictionary of products available from the wholesaler.
                @:key Object of class Product
                @:value List containing product's ID, product's price specific
                for the given Wholesaler, and amount of available products.
        distances : List
            List of distances between the wholesaler and other wholesalers, and the shop.
    '''

    def __init__(self, name: str, id_h: int, dist: List) -> None:
        self.id = id_h
        self.name = name
        self.products = {}
        self.distances = dist

    def add_product_for_wholesaler(self, product: Product, amount: int) -> None:
        """
        Method covering adding a product to wholesaler's assortment.
        :param product: Object of class Product to be added.
        :param amount: Amount of added objects.
        :return: None
        """
        self.products[product.name] = [product.id, product.price + round(uniform(-product.price /2, product.price/2)), amount]


class Shop:
    '''
    Class representing a shop.
        Attributes
        ----------
        max_id_hurt : int
            Maximum ID of a wholesaler assigned so far, incremented once everytime a new Wholesaler is assigned.
        max_id_prod : int
            Maximum ID of a product assigned so far, incremented once everytime a new Product is assigned.
        wholesalers : List[Wholesaler]
            List of wholesalers available to the shop.
        products : Dict[Product : int]
            Dictionary of key-value pairs, key being an object of type Product, and the value being shop's demand for the product.
        cars : List[Car]
            List of cars available to the shop.
    '''

    def __init__(self) -> None:
        self.max_id_hurt = 0
        self.max_id_prod = 0
        self.wholesalers = []
        self.products = {}
        self.cars = []

    def add_wholesaler(self, wholesaler: Wholesaler) -> None:
        """
        Method covering adding a wholesaler to the list of wholesalers available for the shop.
        :param wholesaler: Wholesaler to be added.
        :return: None
        """
        self.wholesalers.append(wholesaler)
        self.max_id_hurt += 1

    def add_product_for_shop(self, product: Product, demand: int) -> None:
        """
        Method covering adding a Product with demand for it to the shop.
        :param product: Product to be added.
        :param demand: Demand for the product being added.
        :return: None
        """
        self.products[product.name] = demand
        self.max_id_prod += 1

    def add_car(self, car: Car):
        """
        Method covering adding an available car for the shop.
        :param car: Car to be added.
        :return: None
        """
        self.cars.append(car)


class Solution:
    """
    @FIXME: Czy my będziemy tego używać?
    """

    def __init__(self) -> None:
        self.m_sol = np.array([])  # macierz ilości produktów pobieranych z konkretnej hurtowni n x i
        self.iteration = 0  # liczba wykonanych iteracji


class Sample:
    """
    Class representing a sample solution of the problem.
        Attributes
        ----------
        shop : Shop
            Object of type Shop for which the solution is being generated.
        cost : float
            Value of the objective function for this particular solution.
        solution : List[List[List[Tuple[Product, int]]]]
            Custom solution form for the solved problem.
            The outermost list consists of solutions to sub-problems of shopping lists for all the cars.
            Each of those shopping lists consists of smaller shopping lists,
            each one concerning a different order from the same or different wholesalers.
            Finally, each of the smallest shopping lists contains pairs of Product objects,
            paired with amount of them being bought in that particular order.
        paths : List[List[int]]
            Custom form representing paths taken by different cars to complete the orders.
            The outermost list contains lists of wholesalers' ID following the specific car's visiting order.
    """

    def __init__(self, shop: Shop, solution: List[List[List[Tuple]]], paths) -> None:
        self.shop = shop
        self.cost = np.inf
        self.solution = solution
        self.paths = paths

    def __str__(self) -> str:  # UWAGA działa tylko gdy liczba produktów we wszystkich hurtowniach jest taka sama
        """
        Method handling printing out solution in a easily readable form to the console.
        :return: Solution in a readable form.
        """
        sol = '====================================\n'
        for c, car in enumerate(self.solution):  # iteracja po samochodach
            sol += f'Samochód {c + 1}\n\n'
            sol += '{:20}'.format('Produkt \ Hurtownia')
            for w in self.paths[c]:  # iteracja po drogach (wypisanie indeksów hurtowni)
                sol += f'{str(w.id)} '
            sol += '\n'
            for p in range(len(self.solution[c][0])):  # iteracja po produktach (kolumnach)
                sol += f'{self.solution[c][0][p][0].name:20}'
                for h in range(len(self.paths[c])):  # iteracja po hurtowniach (wierszach)
                    sol += f'{self.solution[c][h][p][1]:3}  '
                sol += '\n'
            sol += '====================================\n'
        return sol


    def mutation(self, random_change_value: bool = False, random_swap: bool = False, add_or_sub_stop: bool = False,
                 sub_from_val: bool = False) -> List[List[List[Tuple]]]:

        """
        Method handling mutations of sample solutions in the genetic algorithm.
        :param random_change_value: Parameter deciding whether amount of products being bought should change or not.
        :param random_swap: Parameter deciding whether the visiting order for car should change or not.
        :param add_or_sub_stop: Parameter deciding whether one of the wholesalers to visit should be skipped or not.
        :return: Mutated solution.
        """

        if random_change_value:
            car = randint(0, len(self.solution) - 1)
            stop_place = randint(0, len(self.solution[car]) - 1)
            product = randint(0, len(self.solution[car][stop_place]) - 1)
            val = randint(0, 100)
            self.solution[car][stop_place][product] = self.solution[car][stop_place][product][0], val
        elif random_swap:
            car = randint(0, len(self.solution) - 1)
            stop_place_to_swap_1 = randint(0, len(self.solution[car]) - 1)
            stop_place_to_swap_2 = randint(0, len(self.solution[car]) - 1)
            self.solution[car][stop_place_to_swap_1], self.solution[car][stop_place_to_swap_2] = self.solution[car][
                                                                                                     stop_place_to_swap_2], \
                                                                                                 self.solution[car][
                                                                                                     stop_place_to_swap_1]
            self.paths[car][stop_place_to_swap_1], self.paths[car][stop_place_to_swap_2] = self.paths[car][
                                                                                               stop_place_to_swap_2], \
                                                                                           self.paths[car][
                                                                                               stop_place_to_swap_1]
        elif add_or_sub_stop:
            add_or_sub = randint(0, 1)
            car = randint(0, len(self.solution) - 1)
            stop_place = randint(0, len(self.solution[car]))
            if add_or_sub:
                wholesaler = choices(self.shop.wholesalers, k=1)[0]
                self.solution[car].insert(stop_place, [])
                for product_name in wholesaler.products:
                    self.solution[car][stop_place].append((Product(product_name, wholesaler.products[product_name][1], wholesaler.products[product_name][0]), randint(0, np.round(213.7))))
                self.paths[car].insert(stop_place, wholesaler)
            else:
                if len(self.solution[car]) > 1:
                    stop_place = randint(0, len(self.solution[car]) - 1)
                    del self.solution[car][stop_place]
                    del self.paths[car][stop_place]
        elif sub_from_val:
            car = randint(0, len(self.solution) - 1)
            stop_place = randint(0, len(self.solution[car]) - 1)
            product = randint(0, len(self.solution[car][stop_place]) - 1)
            val = randint(0, abs(self.shop.products[self.solution[car][stop_place][product][0].name] -
                                 self.solution[car][stop_place][product][1]))
            if self.shop.products[self.solution[car][stop_place][product][0].name] - self.solution[car][stop_place][product][
                1] < 0:
                val = val * (-1)
            self.solution[car][stop_place][product] = self.solution[car][stop_place][product][0], \
                                                      self.solution[car][stop_place][product][1] + val

        return self.solution


    def objective_function(self, penalty_val: int = 10) -> float:
        """
        Method handling calculation of the sample solution's objective function value.
        Please un-comment print() functions below to see what the course looked like.
        :return: Objective function value for the given sample solution.
        """
        demand = copy.copy(self.shop.products)
        self.cost = 0.0
        # print("========================================================================")
        # print("Starting delivery.")
        for j, car in enumerate(self.solution):
            car_capacity = self.shop.cars[j].capacity
            returns = 0
            sum_weight_of_prod = 0
            # print(
            #     f"Car {j + 1} starts by visiting wholesaler {self.paths[j][0].id}, cost equals {self.paths[j][0].distances[-1]}.")
            self.cost += self.paths[j][0].distances[-1]
            for i, shopping_list in enumerate(car):
                # print(shopping_list)
                for tup in shopping_list:
                    # pass
                    self.cost += tup[1] * self.paths[j][i].products[tup[0].name][1]
                    demand[tup[0].name] -= tup[1]
                    sum_weight_of_prod += tup[1]
                try:
                    # print(
                    #     f"Car {j + 1} is driving from wholesaler {self.paths[j][i].id} to wholesaler {self.paths[j][i + 1].id}, cost equals {self.paths[j][i].distances[self.paths[j][i + 1].id]}.")
                    self.cost += self.paths[j][i].distances[self.paths[j][i + 1].id]
                except:
                    # print(
                    # f"Car {j + 1} driving from wholesaler {self.paths[j][i].id} to shop, cost is {self.paths[j][i].distances[-1]}.")
                    self.cost += self.paths[j][i].distances[-1]
                returns = sum_weight_of_prod // car_capacity
                if returns > 0:
                    sum_weight_of_prod = sum_weight_of_prod % car_capacity
                # print(f"Returns in shop {self.paths[j][i].id} : {returns}")
                self.cost += returns * self.paths[j][0].distances[-1]
        for index, value in enumerate(demand.values()):
            self.cost +=   penalty_val * int(1.1 **(abs(value)//2))
            # print(f"Penalty function value for product: {abs(value) * punish_val} ")
        # print(f"{[self.shop.products[key] for key in self.shop.products.keys()]}")
        # print("Ending delivery.")
        # print("========================================================================")
        return self.cost


class Population:
    """
    Class representing population of sample solutions generated by the genetic algorithm for the problem.
        Attributes
        ----------
        shop : Shop
            Shop for which the solutions are being generated.
        population : List[Sample]
            List holding all the generated solutions, that were not discarded during the algorithm's operation.
        population_size : int
            Size of the generated initial population of sample solutions.
    """

    def __init__(self, shop: Shop, population_size: int) -> None:
        self.shop = shop
        self.population = []
        self.population_size = population_size
        self.generation_counter = 1

    def initial_sample(self):
        """
        Method handling creation of one initial sample solution.
        :param shop: Shop for which the sample solution is being generated.
        :return: None
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
                for product in w.products.keys():
                    solution[car][i].append((Product(product, w.products[product][1], w.products[product][0]), randint(0, np.round(50))))
                i += 1
        return Sample(shop=self.shop, solution=solution, paths=paths)

    def crossover(self, parent1, parent2):
        """
        Method handling crossover of two sample solutions.

        How it works
        ------------
        **Parents**:
        11111111
        00000000
        **Children**:
        11100000
        00011111
        :param **parent1**: First sample solution used to generate a new sample solution.
        :param **parent2**: Second sample solution used to generate a new sample solution.
        :return: None
        """

        child1 = []
        child2 = []
        path_child1 = []
        path_child2 = []
        for car in range(len(parent1.solution)):
            child1.append([]), child2.append([]), path_child1.append([]), path_child2.append([])
            cross_place = randint(0, min(len(parent1.solution[car]), len(parent2.solution[car])))
            for _ in range(len(parent1.solution[car])): child1[car].append([]), path_child1[car].append([])
            for _ in range(len(parent2.solution[car])): child2[car].append([]), path_child2[car].append([])

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
        """
        Method handling generation of the initial population of sample solutions.
        :return: None
        """
        for size in range(self.population_size):
            self.population.append(self.initial_sample())

    def fill_population(self):
        """
        Fill population to population size
        :return:
        """

        while len(self.population) < self.population_size:
            self.population.append(self.initial_sample())

    def sort(self):
        lst = copy.deepcopy(self.population)
        lst_sorted = sorted(lst, key=lambda sample: sample.cost)
        self.population = lst_sorted
        # print(self.population[0])

    def roulette_selection(self):
        # Oblicz sumę wszystkich wartości funkcji przystosowania
        total_fitness = sum(sample.cost for sample in self.population)

        # Losuj liczbę z zakresu od 0 do sumy funkcji przystosowania
        pick = uniform(0, total_fitness)

        # Przeszukaj populację i zwróć osobnika, którego próg zostanie przekroczony
        current = 0
        for sample in self.population:
            current += sample.cost
            if current > pick:
                return sample
