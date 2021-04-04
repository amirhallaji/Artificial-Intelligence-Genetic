import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import csv

# importing the dataset
df = pd.read_csv('births-deaths.csv')

"""
Nations: => Indians, Malayas, Chinese
"""
chinese_df = df.loc[df['ethnic_group'] == 'Chinese']
indians_df = df.loc[df['ethnic_group'] == 'Indians']
malays_df = df.loc[df['ethnic_group'] == 'Malays']
plt.plot(chinese_df['year'], chinese_df['live_births'] - chinese_df['deaths'], color='red')

chinese_df
x_axis = []
for i in range(0, len(chinese_df['year'])):
  x_axis.append((i+1))
print(x_axis)
chinese_df['X_Axis'] = x_axis
chinese_df

years = []
for i in chinese_df['year']:
  years.append(i)

births = []
for i in chinese_df['live_births']:
  births.append(i)

deaths = []
for i in chinese_df['deaths']:
  deaths.append(i)

rate = []
for i in range(len(births)):
  rate.append(births[i]-deaths[i])


with open('chinese.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Year", "X_Axis", "Rate"])
ch = pd.read_csv('chinese.csv')

years = pd.Series(years)
ch['Year'] = years

x_axis = pd.Series(x_axis)
ch['X_Axis'] = x_axis

rate = pd.Series(rate)
ch['Rate'] = rate

chinese_target = list(ch['Rate'])



def initial_population(degree: int, count: int):
    coefficients = []
    for i in range(count):
        cols = []
        for j in range(degree + 1):
            rand = random.randint(0, 100)
            cols.append(rand)
        coefficients.append(cols)
    return coefficients

#-----------------------------------
def crossover(coefficients: list):
    offsprings = []

    random_father = random.sample(range(0, len(coefficients)), len(coefficients))
    random_mother = random.sample(range(0, len(coefficients)), len(coefficients))

    for i in range(0, len(coefficients)):
      father = coefficients[random_father[i]][0:int(len[coefficients[0]])]
      mother = coefficients[random_mother[i]][int(len(coefficients[0])):]
      cols = father + mother
      offsprings.append(cols)

    return offsprings

# ----------------------------------

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


# ----------------------------------

def calc_fitness(population: list, target: list):
    error_values = []
    for i in range(0, len(population)):
        polynomial = np.polyval(population[i], len(population[i]) - 1)
        cols = [polynomial - target[i]]
        error_values.append(cols)

    return population, error_values


# ----------------------------------

def choose_survivals(population: list, error_values: list):
    pop_with_error = []
    for i in range(0, len(population)):
        pop_with_error.append(error_values[i] + population[i])

    pop_with_error.sort(key=lambda x: x[0])

    for i in range(0, int(len(pop_with_error)/5)):
        pop_with_error.pop()


    return pop_with_error


if __name__ == '__main__':
    ip = initial_population(6, 30)
    # for i in range(0, 5):
    ip = mutation(ip)
    ip, err = calc_fitness(ip, chinese_target)
    res = choose_survivals(ip, err)

