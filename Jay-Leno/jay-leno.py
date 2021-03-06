import random


def finalValue(inputs: list):
    finalValue = []
    for i in range(0, len(inputs)):
        cols = [i]
        if len(inputs[i]) == 2:
            cols.append(inputs[i][0])
            cols.append(inputs[i][1])
        else:
            finalVal = inputs[i][1] - inputs[i][2] * inputs[i][3]
            cols.append(inputs[i][0])
            cols.append(finalVal)
        finalValue.append(cols)
    return finalValue

#----------------------------------------
def initialPopulation(N: int):
    size = 2 ** N / 2
    size = int(size)
    population = []
    for i in range(0, size):
        cols = []
        for j in range(0, N):
            rand = random.randint(0, 1)
            cols.append(rand)
        population.append(cols)
    return population

#----------------------------------------

def crossover(population: list):
    """
    for crossover, we perform 1-point crossover.
    """
    offsprings = []
    randomFather = random.sample(range(0, len(population)), len(population))
    randomMother = random.sample(range(0, len(population)), len(population))
    point = int(len(population[0]) / 2)
    for i in range(0, len(population)):
        newGenes = []
        for j in range(0, point):
            father = (population[randomFather[i]][0:(j + 1)])[::]
            mother = (population[randomMother[i]][(j + 1):])[::]
            newGenes.append(father + mother)
        offsprings.append(newGenes)
    result = []
    for i in offsprings:
        for j in i:
            result.append(j)
    return result

#----------------------------------------

def mutation(offspring: list):
    """
    Here, for mutation, I chose bit-flipping, which is implemented below:
    Randomly, choose 1/n of the population and toggle one of the random bits of them.
    """
    randomPositions = random.sample(range(0, len(offspring[0])), int(len(offspring[0])))

    randomBits = random.sample(range(0, len(offspring[0])), len(offspring[0]))

    for i in range(0, len(randomPositions)):
        if offspring[randomPositions[i]][randomBits[i]] == 1:
            offspring[randomPositions[i]][randomBits[i]] = 0
        else:
            offspring[randomPositions[i]][randomBits[i]] = 1
    return offspring

#----------------------------------------

def calcFitness(population: list, priceVal: list, initialMoney: int):
    copyOfMoney = initialMoney
    populationWithIndex = []
    index = []
    for i in range(0, len(population)):
        cols = [i]
        index.append(cols)

    for i in range(0, len(population)):
        populationWithIndex.append(index[i] + population[i])

    scores = []

    for i in range(0, len(population)):
        initialMoney = copyOfMoney
        efficiency = 0
        for j in range(0, len(population[0])):
            if population[i][j] == 1:
                initialMoney -= priceVal[j][1]  # money - price
                efficiency += priceVal[j][2]  # +value
        if initialMoney >= 0:
            scores.append(efficiency)
        else:
            scores.append(-1)
    return populationWithIndex, scores
#----------------------------------------

def chooseSurvivals(populationWithIndex: list, scores: list):

    """
    First, we have to combine population list and scores in one list in order to sort them
    according to the ascending scores as our survivals.
    """
    scoresList = []
    for i in range(0, len(scores)):
        cols = [scores[i]]
        scoresList.append(cols)

    listOfScoresAndPop = []
    for i in range(0, len(populationWithIndex)):
        listOfScoresAndPop.append(scoresList[i] + populationWithIndex[i])
    listOfScoresAndPop.sort(key=lambda x: -x[0])


    """
    For the next generation, we remove the 20% of the worst and send others to crossover
    for the next generation.
    """
    nextGeneration = []

    for i in range(0, len(listOfScoresAndPop[0])-2):
        listOfScoresAndPop.pop()

    for i in range(0, len(listOfScoresAndPop)):
        nextGeneration.append(listOfScoresAndPop[i][2:])

    return nextGeneration

# ----------------------------------------

if __name__ == '__main__':
    initialMoney = input()
    initialMoney = int(initialMoney)

    # count of cars
    N = input()
    N = int(N)

    listOfInputs = []
    for i in range(0, N):
        listOfInputs.append(list(map(int, input().split())))

    finalVal = finalValue(listOfInputs)
    pop = initialPopulation(N)
    for i in range(0, len(pop[0])):
        pop = crossover(pop)
        pop = mutation(pop)
        popWithIndex, score = calcFitness(pop, finalVal, initialMoney)
        pop = chooseSurvivals(popWithIndex, score)

    for i in range(0, len(pop[0])):
        print(pop[0][i], end='\n')


