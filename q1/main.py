import random

#
# def calculateFinalValue(price: list):
#     finalDetails = []
#     for carIndex in range(0, len(price)):
#         cols = [carIndex, price[carIndex][0]]
#         finalValue = price[carIndex][1] - price[carIndex][2] * price[carIndex][3]
#         cols.append(finalValue)
#         finalDetails.append(cols)
#     return finalDetails

def initializePopulation():
    initialPopulation = []

    for i in range(0, 1000):
        cols = [i]
        price = random.randint(10, 1000)
        cols.append(price)
        value = random.randint(0, price)
        cols.append(value)
        initialPopulation.append(cols)
    return initialPopulation

def calculateFitness(population: list):
    fitnessList = []
    for i in range(0, len(population)):
        cols = [i]
        fitness = population[i][2] - population[i][1]
        cols.append(fitness)
        fitnessList.append(cols)
    return fitnessList

def crossover(population: list):
    randomFather = random.sample(range(0, len(population)), len(population))
    randomMother = random.sample(range(0, len(population)), len(population))

    offsprings = population[::]
    for i in range(0, len(randomFather)):
        cols = [i, population[randomFather[i]][1], population[randomMother[i]][2]]
        offsprings.append(cols)
    return offsprings

def mutation(population: list):
    """
     since the problem is in Integer Representation,
     I chose Creeping in mutation, which is adding a positive or negative number
     with the probability of pm.
    """
    randomCreeps = []
    for i in range(0, int(len(population)/5)):
        randomCreeps.append(random.randint(-5, 5))

    randomPositions = random.sample(range(0, int(len(population)/5)), int(len(population)/5))

    for i in range(0, len(randomPositions)):
        population[randomPositions[i]][1] += randomCreeps[i]

    return population

def chooseSurvivals(population: list):
    survivals = []
    for i in range(0, len(population)):
        if -10 < population[i][2] - population[i][1]  and population[i][2] <= population[i][1]:
            survivals.append(population[i])
    return survivals

if __name__ == '__main__':
    pop = initializePopulation()

    for i in range(0, 5):
        pop = crossover(pop)
        pop = mutation(pop)
        pop = chooseSurvivals(pop)
    print(pop)

    # listOfAll = []
    # firstAsset = input()
    # firstAsset = int(firstAsset)
    #
    # carCount = input(int)
    # carCount = int(carCount)
    #
    # for i in range(0, carCount):
    #     cols = []
    #     carPrice = input()
    #     carPrice = int(carPrice)
    #     cols.append(carPrice)
    #
    #     earlyValue = input()
    #     earlyValue = int(earlyValue)
    #     cols.append(earlyValue)
    #
    #     distance = input()
    #     distance = int(distance)
    #     cols.append(distance)
    #
    #     decreaseRate = input() # enter 0 if not wanted.
    #     decreaseRate = int(decreaseRate)
    #     cols.append(decreaseRate)
    #
    #     listOfAll.append(cols)



