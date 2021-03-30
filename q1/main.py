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




if __name__ == '__main__':
    listOfAll = []
    firstAsset = input()
    firstAsset = int(firstAsset)

    carCount = input(int)
    carCount = int(carCount)

    for i in range(0, carCount):
        cols = []
        carPrice = input()
        carPrice = int(carPrice)
        cols.append(carPrice)

        earlyValue = input()
        earlyValue = int(earlyValue)
        cols.append(earlyValue)

        distance = input()
        distance = int(distance)
        cols.append(distance)

        decreaseRate = input() # enter 0 if not wanted.
        decreaseRate = int(decreaseRate)
        cols.append(decreaseRate)

        listOfAll.append(cols)



