"""
    ESERCIZIO 3.12
    Scrivi un programma in Python che plotti una distribuzione di Poisson. Mostra, usando i metodi per calcolare il terzo e il quarto momento centrale della libreria
    scipy.stats, che i momenti della distribuzione di Poisson tendono asintoticamente a quelli di una gaussiana.
"""

# Librerie
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import poisson

def main():

    # Parametri poissoniana
    mu = 6.0

    # Funzioni da plottare
    x_coord = np.arange(20)
    poiss = poisson(mu)

    # Plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 12")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    plt.plot(x_coord, poiss.pmf(x_coord), "o-", label = "pmf(x)", color = "red")
    plt.savefig("poisson.png")

    # Liste skewness e kurtosi
    skew_list = []
    kurt_list = []

    for i in range(10000):
        poiss = poisson(i)
        skew, kurt = poiss.stats(moments = "sk")
        skew_list.append(skew)
        kurt_list.append(kurt)

    # Plot dei momenti
    x_coord = np.arange(10000)
    plt.clf()
    plt.plot(x_coord, skew_list, "-", label = "skewness", color = "blue")
    plt.plot(x_coord, kurt_list, "-", label = "kurtosi", color = "red")
    plt.legend()
    plt.savefig("poisson_momenti.png")

    return

if __name__ == "__main__":
    main()