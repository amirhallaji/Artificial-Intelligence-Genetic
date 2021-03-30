import random

initialMoney = None
# maximumEfficiency = -initialMoney

def calculateInitialPopulation(inputs: list):
    initialPopulation = []
    for i in range(0, len(inputs)):
        cols = [i]
        if len(inputs[i]) == 2:
            cols.append(inputs[i][0])
            cols.append(inputs[i][1])
        else:
            finalValue = inputs[i][1] - inputs[i][2] * inputs[i][3]
            cols.append(inputs[i][0])
            cols.append(finalValue)
        initialPopulation.append(cols)
    return initialPopulation

# ------------------------------------------

def crossover(population: list):
    randomFather = random.sample(range(0, len(population)), len(population))
    randomMother = random.sample(range(0, len(population)), len(population))

    offsprings = []
    for i in range(0, len(randomFather)):
        cols = [i, population[randomFather[i]][1], population[randomMother[i]][2]]
        offsprings.append(cols)
    return offsprings
#--------------------------------------------

def mutation(population: list):
    """
     Since the representation of this genetic problem is Integer form,
     I chose Creeping in mutation, which is adding a positive or negative number
     with the probability of pm to a random population.
    """
    randomCreeps = []
    for i in range(0, int(len(population)/5)):
        randomCreeps.append(random.randint(-5, 5))

    randomPositions = random.sample(range(0, int(len(population)/5)), int(len(population)/5))

    for i in range(0, len(randomPositions)):
        population[randomPositions[i]][1] += randomCreeps[i]

    return population
#---------------------------------------------
def chooseSurvivals(population: list):
    nextPopulation = []
    currentDiversity = 0
    for i in range(0, len(population)):
        if -10 < population[i][1] - population[i][2] < 10:
            nextPopulation.append(i)
            nextPopulation.append(population[i][1])
            nextPopulation.append(population[i][2])
        # currentDiversity += population[i][1] - population[i][2]
    return nextPopulation

#----------------------------------------------

if __name__ == '__main__':

    initialMoney = input()
    initialMoney = int(initialMoney)

    # count of cars
    N = input()
    N = int(N)

    listOfInputs = []
    for i in range(0, N):
        listOfInputs.append(list(map(int, input().split())))

    print(listOfInputs)
    pop = calculateInitialPopulation(listOfInputs)
    for i in range(0, 5):
        pop = crossover(pop)
        pop = mutation(pop)
        pop = chooseSurvivals(pop)
    print(pop)





