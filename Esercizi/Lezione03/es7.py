"""
    ESERCIZIO 3.7
    Scrivi un programma in Python che plotti una PDF gaussiana e la sua CDF
"""

# Librerie
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

def main():

    # Parametri gaussiana
    media = 0.0
    devstd = 0.5

    # Funzioni da plottare
    x_min = -3.0
    x_max = 3.0
    x_coord = np.linspace(x_min, x_max, 1000000)
    gauss = norm(media, devstd)

    # Plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("PDF e CDF gaussiane")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.plot(x_coord, gauss.pdf(x_coord), label = "pdf(x)", color = "blue")
    plt.plot(x_coord, gauss.cdf(x_coord), label = "cdf(x)", color = "red")
    ax.legend()
    plt.show()

    return

if __name__ == "__main__":
    main()