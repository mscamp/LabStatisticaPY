"""
    ESERCIZIO 4.4
    Implementa un generatore di numeri pseudo-casuali distribuiti uniformemente in un dato intervallo. Usa matplotlib per visualizzare
    la distribuzione dei numeri generati.
"""

# Librerie
import numpy as np
from random import random
from matplotlib import pyplot as plt

def sturges(n_eventi: int) -> int:
    return int(np.ceil(1.0 + 3.322 * np.log(n_eventi)))

def rand_range(x_min: float, x_max: float) -> float:
    return (x_min + (x_max - x_min) * random())

def main() -> None:

    # Variabili
    x_min: float = 0.0
    x_max: float = 10.0
    unif_sequence: list[float] = []

    # Genera la sequenza di numeri pseudo-casuali uniformi
    for i in range(150000):
        unif_sequence.append(rand_range(x_min, x_max))

    # Plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 4")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Istogramma
    n_bins: int = sturges(len(unif_sequence))
    bin_edges = np.linspace(x_min, x_max, n_bins)
    ax.hist(unif_sequence, bin_edges, color = "orange")

    plt.show()

    return

if __name__ == "__main__":
    main()