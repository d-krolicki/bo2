from structure import *
import matplotlib.pyplot as plt

"""
Wydaje mi sie, ze powinno przyjmowac argument po prostu obiekt typu Shop, a zwracac obiekt typu Solution.
"""

CROSSOVER_PROBABILITY = 0.98
MUTATION_PROBABILITY_SWAP_AMOUNT = 0.001
MUTATION_PROBABILITY_VISIT_ORDER = 0.001
MUTATION_PROBABILITY_ADD_OR_REMOVE_POINT = 0.001
MUTATION_PROBABILITY_SUBTRACT_AMOUNT = 0.1


def algo(shop: Shop, iterationStop: int = 1000, populationSize: int = 300, penaltyVal: int = 2) -> Solution:
    zmiana_najlepszego_osobnika = []
    toplot = []
    test = Population(shop, populationSize)
    test.initial_population()
    for s in range(populationSize):
        test.population[s].objective_function(penaltyVal)
    test.sort() 
    najlepszy = test.population[0]
    for i in range(iterationStop):
        
        
        newPopulation = []
        for s in range(0,int((populationSize)/2)):
            crossP = random()

            if crossP < CROSSOVER_PROBABILITY:
                # print(test.population[s])
                child1, child2 = test.crossover(test.roulette_selection(), test.roulette_selection())
                newPopulation.append(child1)
                newPopulation.append(child2)
        test.population = newPopulation
        print(i) 
        test.fill_population()

        for s in range(populationSize):
            mutation1P = random()
            mutation2P = random()
            mutation3P = random()
            mutation4P = random()

            if mutation1P < MUTATION_PROBABILITY_SWAP_AMOUNT:
                test.population[s].mutation(True, False, False, False)

            if mutation2P < MUTATION_PROBABILITY_VISIT_ORDER:
                test.population[s].mutation(False, True, False, False)

            if mutation3P < MUTATION_PROBABILITY_ADD_OR_REMOVE_POINT:
                test.population[s].mutation(False, False, True, False)

            if mutation4P < MUTATION_PROBABILITY_SUBTRACT_AMOUNT:
                test.population[s].mutation(False, False, False, True)

        for s in range(populationSize):
            test.population[s].objective_function(penaltyVal)
        
        test.sort()
        toplot.append(test.population[0].cost)
        if najlepszy.cost>test.population[0].cost:
            najlepszy = test.population[0]
        zmiana_najlepszego_osobnika.append(najlepszy.cost)
        
    plt.plot(zmiana_najlepszego_osobnika)
    plt.show()

    return najlepszy

