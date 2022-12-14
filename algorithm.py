from typing import List, Union, Any, Tuple
from structure import *
import matplotlib.pyplot as plt

from structure import Sample


def algo(shop: Shop, iterationStop: int = 10, populationSize: int = 10, probablityM1: float = 0.1,
         probablityM2: float = 0.1, probablityM3: float = 0.1, probablityM4: float = 0.1, probabilityC: float = 0.1,
         penaltyVal: int = 10) -> Tuple[Any, List[Any]]:
    CROSSOVER_PROBABILITY = probabilityC
    MUTATION_PROBABILITY_SWAP_AMOUNT = probablityM1
    MUTATION_PROBABILITY_VISIT_ORDER = probablityM2
    MUTATION_PROBABILITY_ADD_OR_REMOVE_POINT = probablityM3
    MUTATION_PROBABILITY_SUBTRACT_AMOUNT = probablityM4

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

        for s in range(0, int(populationSize / 2)):
            crossP = random()

            if crossP < CROSSOVER_PROBABILITY:
                child1, child2 = test.crossover(test.roulette_selection(), test.roulette_selection())
                newPopulation.append(child1)
                newPopulation.append(child2)
        test.population = newPopulation
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

        if najlepszy.cost > test.population[0].cost:
            najlepszy = test.population[0]
        zmiana_najlepszego_osobnika.append(najlepszy.cost)

    return najlepszy, zmiana_najlepszego_osobnika


def algo2(shop: Shop, iterationStop: int = 10, populationSize: int = 100, probablityM1: float = 0.1,
          probablityM2: float = 0.1, probablityM3: float = 0.1, probablityM4: float = 0.1, probabilityC: float = 0.1,
          changesInPopulationValue: int = 80, penaltyVal: int = 100) -> List[Union[List[Any], Any]]:
    test = Population(shop, populationSize)  # inicjalizowanie polulacji
    test.initial_population()  # tworzenie pierwszej poplacji losowej

    CROSSOVER_PROBABILITY = probabilityC
    MUTATION_PROBABILITY_SWAP_AMOUNT = probablityM1
    MUTATION_PROBABILITY_VISIT_ORDER = probablityM2
    MUTATION_PROBABILITY_ADD_OR_REMOVE_POINT = probablityM3
    MUTATION_PROBABILITY_SUBTRACT_AMOUNT = probablityM4
    toplot = []
    calculate_cost_fun(test, penaltyVal)  # obliczanie funkcji celu do osobnik??w oraz sortowanie
    while iterationStop > 0:  # liczba iteracji STOP
        changesInPopulation = changesInPopulationValue
        while changesInPopulation > 0:  # liczba podj??tych pr??b zmian w populacji

            # prawdopodobie??stwa mutacji i krzy????wki
            mutation1P = random()
            mutation2P = random()
            mutation3P = random()
            mutation4P = random()
            crossoverP = random()

            if mutation1P < MUTATION_PROBABILITY_SWAP_AMOUNT:  # czy mutacja ma si?? wykona???
                s = fractional_probability(test)  # wybieranie osobnika do mutacji
                tempSample = copy.deepcopy(test.population[s])  # skopiowanie osobnika
                tempSample.mutation(True, False, False, False)  # wykonanie mutacji osobnika
                tempSample.objective_function(penaltyVal)  # obliczenie jego funkcji celu
                if tempSample.cost < test.population[-1].cost:  # dodanie do populacji je??li jest lepszy od najgorszego
                    test.population[-1] = tempSample
                    for i in range(1, test.population_size):
                        poprz = -i - 1
                        if test.population[-i].cost < test.population[poprz].cost:
                            test.population[-i], test.population[poprz] = test.population[poprz], test.population[-i]
                        else:
                            break

            if mutation2P < MUTATION_PROBABILITY_VISIT_ORDER:
                s = fractional_probability(test)
                tempSample = copy.deepcopy(test.population[s])
                tempSample.mutation(False, True, False, False)
                tempSample.objective_function(penaltyVal)
                if tempSample.cost < test.population[-1].cost:
                    test.population[-1] = tempSample
                    for i in range(1, test.population_size):
                        poprz = -i - 1
                        if test.population[-i].cost < test.population[poprz].cost:
                            test.population[-i], test.population[poprz] = test.population[poprz], test.population[-i]
                        else:
                            break

            if mutation3P < MUTATION_PROBABILITY_ADD_OR_REMOVE_POINT:
                s = fractional_probability(test)
                tempSample = copy.deepcopy(test.population[s])
                tempSample.mutation(False, False, True, False)
                tempSample.objective_function(penaltyVal)
                if tempSample.cost < test.population[-1].cost:
                    test.population[-1] = tempSample
                    for i in range(1, test.population_size):
                        poprz = -i - 1
                        if test.population[-i].cost < test.population[poprz].cost:
                            test.population[-i], test.population[poprz] = test.population[poprz], test.population[-i]
                        else:
                            break

            if mutation4P < MUTATION_PROBABILITY_SUBTRACT_AMOUNT:
                s = fractional_probability(test)
                tempSample = copy.deepcopy(test.population[s])
                tempSample.mutation(False, False, False, True)
                tempSample.objective_function(penaltyVal)
                if tempSample.cost < test.population[-1].cost:
                    test.population[-1] = tempSample
                    for i in range(1, test.population_size):
                        poprz = -i - 1
                        if test.population[-i].cost < test.population[poprz].cost:
                            test.population[-i], test.population[poprz] = test.population[poprz], test.population[-i]
                        else:
                            break
            if crossoverP < CROSSOVER_PROBABILITY:
                s1 = fractional_probability(test)
                s2 = fractional_probability(test)
                child1, child2 = test.crossover(copy.deepcopy(test.population[s1]), copy.deepcopy(test.population[s2]))
                child1.objective_function(penaltyVal)
                child2.objective_function(penaltyVal)
                test.population.append(child1)
                test.population_size = len(test.population)
                for i in range(1, test.population_size):
                    poprz = -i - 1
                    if test.population[-i].cost < test.population[poprz].cost:
                        test.population[-i], test.population[poprz] = test.population[poprz], test.population[-i]
                    else:
                        break
                test.population.append(child2)
                test.population_size = len(test.population)
                for i in range(1, test.population_size):
                    poprz = -i - 1
                    if test.population[-i].cost < test.population[poprz].cost:
                        test.population[-i], test.population[poprz] = test.population[poprz], test.population[-i]
                    else:
                        break
                test.population = test.population[:-2]
                test.population_size = len(test.population)

            changesInPopulation -= 1

        toplot.append(test.population[0].cost)
        iterationStop -= 1

    return [test.population[0], toplot]


def fractional_probability(population: Population):  # wybieranie osobnik??w do mutacji/krzy????wki
    costSum = 0
    for idx in range(population.population_size):  # obliczanie sumy funkcji celu
        costSum += population.population[idx].cost

    acc = 0  # sumy prawdopodobie??stwa
    propOfChoice = random()
    for sampleIDX in range(population.population_size):
        acc += (1 - population.population[sampleIDX].cost / costSum)
        if propOfChoice < acc:
            return sampleIDX


def calculate_cost_fun(population: Population, penaltyVal: int = 10) -> None:
    for s in range(population.population_size):
        population.population[s].objective_function(penaltyVal)  # obliczanie funkcji celu dla populacji
    population.sort()  # sortowanie populacji
