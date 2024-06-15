"""
    ESERCIZIO 3.10
    Scrivi un programma in Python che plotti una distribuzione binomiale e la sua CDF
"""

# Librerie
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import binom

def main():

    # Parametri binomiale
    n = 10
    p = 0.7 

    # Funzioni da plottare
    x_coord = np.arange(n + 1)
    binomiale = binom(n, p)

    # Plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("PMF e CDF binomiali")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.scatter(x_coord, binomiale.pmf(x_coord), label = "pmf(x)", color = "blue")
    plt.scatter(x_coord, binomiale.cdf(x_coord), label = "cdf(x)", color = "red")
    ax.legend()

    plt.show()

    return

if __name__ == "__main__":
    main()