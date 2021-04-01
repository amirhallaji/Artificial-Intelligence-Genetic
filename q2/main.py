import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rand

class Individual:

    def __init__(self, degree):
        coefficient = []
    #-----------------------------

    def calcFitness(self):
        self.fitness = 0



if __name__ == '__main__':

    # importing dataset
    df = pd.read_csv('births-deaths.csv')
    plt.plot(df['year'], df['live_births'])
