from structure import *
from random import randint
import matplotlib.pyplot as plt

"""
Wydaje mi sie, ze powinno przyjmowac argument po prostu obiekt typu Shop, a zwracac obiekt typu Solution.
"""

CROSSOVER_PROBABILITY = 0.5
MUTATION_PROBABILITY_SWAP_AMOUNT = 0.01
MUTATION_PROBABILITY_VISIT_ORDER = 0.01
MUTATION_PROBABILITY_ADD_OR_REMOVE_POINT = 0.01
COUNTER = 0


def algo(shop: Shop, iterationStop: int = 1000, populationSize: int = 50, penaltyVal: int = 10) -> Solution:
    toplot = []
    test = Population(shop, populationSize)
    test.initial_population()
    for s in range(populationSize):
        test.population[s].objective_function(penaltyVal)
    test.sort()
    for i in range(iterationStop):

        newPopulation = []
        for s in range(0, int((populationSize - 1))):
            crossP = random()

            if crossP < CROSSOVER_PROBABILITY:
                # print(test.population[s])
                child1, child2 = test.crossover(test.population[s], test.population[s + 1])
                newPopulation.append(child1)
                newPopulation.append(child2)
        test.population = newPopulation
        print(i)
        test.fill_population()

        for s in range(populationSize):
            mutation1P = random()
            mutation2P = random()
            mutation3P = random()

            if mutation1P < MUTATION_PROBABILITY_SWAP_AMOUNT:
                test.population[s].mutation(True, False, False)

            if mutation2P < MUTATION_PROBABILITY_VISIT_ORDER:
                test.population[s].mutation(False, True, False)

            if mutation3P < MUTATION_PROBABILITY_ADD_OR_REMOVE_POINT:
                test.population[s].mutation(False, False, True)

        for s in range(populationSize):
            test.population[s].objective_function(penaltyVal)

        test.sort()
        toplot.append(test.population[0].cost)

    plt.plot(toplot)
    plt.show()

    return test.population[0].cost


def algo2(shop: Shop, iterationStop: int = 50, changesInPopulationValue: int = 80, populationSize: int = 100,
          penaltyVal: int = 10) -> Solution:
    test = Population(shop, populationSize)  # inicjalizowanie polulacji
    test.initial_population()  # tworzenie pierwszej poplacji losowej

    toplot = []

    while iterationStop > 0:  # liczba iteracji STOP
        changesInPopulation = changesInPopulationValue
        while changesInPopulation > 0:  # liczba podjętych prób zmian w populacji
            calculate_cost_fun(test, penaltyVal)  # obliczanie funkcji celu do osobników oraz sortowanie

            # prawdopodobieństwa mutacji i krzyżówki
            mutation1P = random()
            mutation2P = random()
            mutation3P = random()
            crossoverP = random()

            if mutation1P < MUTATION_PROBABILITY_SWAP_AMOUNT:  # czy mutacja ma się wykonać?
                s = fractional_probability(test)  # wybieranie osobnika do mutacji
                tempSample = copy.deepcopy(test.population[s])  # skopiowanie osobnika
                tempSample.mutation(True, False, False)  # wykonanie mutacji osobnika
                tempSample.objective_function(penaltyVal)  # obliczenie jego funkcji celu
                if tempSample.cost < test.population[-1].cost:  # dodanie do populacji jeśli jest lepszy od najgorszego
                    test.population[-1] = tempSample
                test.sort()  # sortowanie

            if mutation2P < MUTATION_PROBABILITY_VISIT_ORDER:
                s = fractional_probability(test)
                tempSample = copy.deepcopy(test.population[s])
                tempSample.mutation(False, True, False)
                tempSample.objective_function(penaltyVal)
                if tempSample.cost < test.population[-1].cost:
                    test.population[-1] = tempSample
                test.sort()

            if mutation3P < MUTATION_PROBABILITY_ADD_OR_REMOVE_POINT:
                s = fractional_probability(test)
                tempSample = copy.deepcopy(test.population[s])
                tempSample.mutation(False, False, True)
                tempSample.objective_function(penaltyVal)
                if tempSample.cost < test.population[-1].cost:
                    test.population[-1] = tempSample
                test.sort()

            # if crossoverP < CROSSOVER_PROBABILITY:
            #     s1 = fractional_probability(test)
            #     s2 = fractional_probability(test)
            #     child1, child2 = test.crossover(test.population[s1], test.population[s2])
            #     print(child1)
            #     print(child2)
            #     child1.objective_function(penaltyVal)
            #     child2.objective_function(penaltyVal)
            #
            #     test.population.append(child2)
            #     test.population_size += 2
            #     calculate_cost_fun(test, penaltyVal)
            #     test.population_size -= 2
            #     test.population = test.population[:-2]

            calculate_cost_fun(test, penaltyVal)
            changesInPopulation -= 1

        toplot.append(test.population[0].cost)
        iterationStop -= 1

    plt.plot(toplot)
    plt.show()

    return test.population[0].cost


def fractional_probability(population: Population):  # wybieranie osobników do mutacji/krzyżówki
    costSum = 0
    for idx in range(population.population_size):  # obliczanie sumy funkcji celu
        costSum += population.population[idx].cost

    acc = 0  # sumy prawdopodobieństwa
    propOfChoice = random()
    for sampleIDX in range(population.population_size):
        acc += (1 - population.population[sampleIDX].cost / costSum)
        if propOfChoice < acc:
            return sampleIDX


def calculate_cost_fun(population: Population, penaltyVal: int = 10) -> None:
    for s in range(population.population_size):
        population.population[s].objective_function(penaltyVal)  # obliczanie funkcji celu dla populacji
    population.sort()  # sortowanie populacji
