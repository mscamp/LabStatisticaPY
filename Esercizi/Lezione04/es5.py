"""
    ESERCIZIO 4.5
    Implementa un generatore di numeri pseudo-casuali che utilizzi il metodo TAC per generare numeri pseudo-casuali distribuiti secondo
    una distribuzione di probabilità arbitraria. Il generatore deve prendere come input la PDF. Usa matplotlib per visualizzare la 
    distribuzione dei numeri generati.
"""

# Librerie
import numpy as np
from random import random
from matplotlib import pyplot as plt
from scipy.stats import expon

def sturges(n_eventi: int) -> int:
    return int(np.ceil(1.0 + 3.322 * np.log(n_eventi)))

def rand_range(x_min: float, x_max: float) -> float:
    return x_min + (x_max - x_min) * random()

def rand_TAC(f, x_min: float, x_max: float, y_max: float) -> float:
    """ Genera un numero pseudo-casuale distribuito secondo la PDF "f" nell'intervallo di estremi x_min e x_max """

    x = rand_range(x_min, x_max)
    y = rand_range(0, y_max)

    while y > f(x):
        x = rand_range(x_min, x_max)
        y = rand_range(0, y_max)

    return x

def main() -> None:

    # Variabili
    exp_events: list[float] = []
    x_min: float = 0.0
    x_max: float = 5.0

    # PDF
    mu: float = 0.0
    exp_pdf = expon(mu)

    # Genera numeri esponenziali
    for i in range(10000):
        exp_events.append(rand_TAC(exp_pdf.pdf, x_min, x_max, exp_pdf.pdf(mu)))

    # Plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 5")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Istogramma
    n_bins: int = sturges(len(exp_events))
    bin_edges = np.linspace(x_min, x_max, n_bins)
    ax.hist(exp_events, bin_edges, color = "orange")

    plt.show()

    return

if __name__ == "__main__":
    main()