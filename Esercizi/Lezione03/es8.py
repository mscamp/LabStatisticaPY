"""
    ESERCIZIO 3.8
    Scrivi un programma in Python che plotti una PDF esponenziale e la sua CDF
"""

# Librerie
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import expon

def main():

    # Parametri esponenziale
    media = 0.0
    devstd = 1.5

    # Funzioni da plottare
    x_min = 0.0
    x_max = 8.0
    x_coord = np.linspace(x_min, x_max, 1000000)
    exp = expon(media, devstd)

    # Plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("PDF e CDF esponenziali")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.plot(x_coord, exp.pdf(x_coord), label = "pdf(x)", color = "blue")
    plt.plot(x_coord, exp.cdf(x_coord), label = "cdf(x)", color = "red")
    ax.legend()
    plt.show()

    return

if __name__ == "__main__":
    main()