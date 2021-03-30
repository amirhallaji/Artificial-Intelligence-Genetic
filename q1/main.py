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
        value = random.randint(10, 1000)
        cols.append(price)
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

    offsprings = []
    for i in range(0, len(randomFather)):
        cols = [i, population[randomFather[i]][1], population[randomMother[i]][2]]
        offsprings.append(cols)
    return offsprings



if __name__ == '__main__':
    pop = initializePopulation()
    print(pop)
    print(calculateFitness(pop))
    off = crossover(pop)
    print(off)
    print(len(off))

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



