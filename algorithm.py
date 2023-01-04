from structure import *
from random import randint
import matplotlib.pyplot as plt

"""
Wydaje mi sie, ze powinno przyjmowac argument po prostu obiekt typu Shop, a zwracac obiekt typu Solution.
"""

CROSSOVER_PROBABILITY = 0.98
MUTATION_PROBABILITY_SWAP_AMOUNT = 0.0005
MUTATION_PROBABILITY_VISIT_ORDER = 0.005
MUTATION_PROBABILITY_ADD_OR_REMOVE_POINT = 0.0005


def algo(shop: Shop, iterationStop: int = 1000, populationSize: int = 50, penaltyVal: int = 10) -> Solution:
    toplot = []
    test = Population(shop, populationSize)
    test.initial_population()
    for s in range(populationSize):
        test.population[s].objective_function(penaltyVal)
    test.sort()   
    for i in range(iterationStop):
        
        
        newPopulation = []
        for s in range(0,int((populationSize-1))):
            crossP = random()

            if crossP < CROSSOVER_PROBABILITY:
                # print(test.population[s])
                child1, child2 = test.crossover(test.population[s], test.population[s+1])
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
