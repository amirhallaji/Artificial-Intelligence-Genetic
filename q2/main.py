import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

def initial_population(degree: int, count: int):
    coefficients = []
    for i in range(count):
        cols = []
        for j in range(degree+1):
            rand = random.randint(0, 100)
            cols.append(rand)
        coefficients.append(cols)
    return coefficients

#----------------------------------

def mutation(coefficients: list):
    random_positions = random.sample(range(0, len(coefficients)), len(coefficients[0]))
    random_poly = random.sample(range(0, len(coefficients[0])), len(coefficients[0]))

    for i in range(0, len(random_positions)):
        add_or_minus = random.randint(0, 1)
        if add_or_minus == 1:
            coefficients[random_positions[i]][random_poly[i]] += 5
        else:
            coefficients[random_positions[i]][random_poly[i]] -= 5
    return coefficients
#----------------------------------

def calc_fitness(population: list, target: list):
    error_values = []
    for i in range(0, len(population)):
        polynomial = np.polyval(population[i], len(population[i])-1)
        error_values.append(polynomial - target[i])
    return population, error_values

#----------------------------------

def choose_survivals(population: list, error_values: list):
    pop_with_error = []
    for i in range(0, len(population)):
        pop_with_error.append(population[i] + error_values[i])

    pop_with_error.sort(key=lambda x: -x[-1])
    return pop_with_error

if __name__ == '__main__':

    # # importing dataset
    # df = pd.read_csv('births-deaths.csv')
    # plt.plot(df['year'], df['live_births'])
    r = initial_population(4, 6)
    print(r)
    r = mutation(r)
    print(r)
    r, main_v = calc_fitness(r, [1, 2, 3, 4, 5, 6])
    print(r)
    print(main_v)
