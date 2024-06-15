"""
    ESERCIZIO 3.11
    Scrivi un programma di Python che plotti la distribuzione di Poisson per diversi valori della sua media, sovrapposte
"""

# Librerie
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import poisson

def main():

    # Parametri della poissoniana
    mu_1 = 1.5
    mu_2 = 3.0 
    mu_3 = 4.5 
    mu_4 = 6.0 
    mu_5 = 7.5

    # Funzioni da plottare
    x_coord = np.arange(20) 
    poiss_1 = poisson(mu_1)
    poiss_2 = poisson(mu_2)
    poiss_3 = poisson(mu_3)
    poiss_4 = poisson(mu_4)
    poiss_5 = poisson(mu_5)

    # Plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Distribuzione poissoniana")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.plot(x_coord, poiss_1.pmf(x_coord), "o-", label = "pmf_1(x)", color = "blue")
    plt.plot(x_coord, poiss_2.pmf(x_coord), "o-", label = "pmf_2(x)", color = "violet")
    plt.plot(x_coord, poiss_3.pmf(x_coord), "o-", label = "pmf_3(x)", color = "green")
    plt.plot(x_coord, poiss_4.pmf(x_coord), "o-", label = "pmf_4(x)", color = "red")
    plt.plot(x_coord, poiss_5.pmf(x_coord), "o-", label = "pmf_5(x)", color = "orange")

    plt.show()

    return

if __name__ == "__main__":
    main()