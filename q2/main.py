import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    # importing dataset
    df = pd.read_csv('births-deaths.csv')
    plt.plot(df['year'], df['live_births'])
