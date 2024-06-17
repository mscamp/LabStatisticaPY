"""
    ESERCIZIO 4.6
    Implementa un generatore di numeri pseudo-casuale che usi il metodo della funzione inversa per generare eventi distribuiti secondo
    una distribuzione di probabilità esponenziale. Usa matplotlib per visualizzare la distribuzione dei numeri generati.
"""

# Librerie
import numpy as np
from random import random
from matplotlib import pyplot as plt

def sturges(n_eventi: int) -> int:
    return int(np.ceil(1.0 + 3.322 * np.log(n_eventi)))

def rand_range(x_min: float, x_max: float) -> float:
    return x_min + (x_max - x_min) * random()

def inverse_exponential_CDF(y: float, mu: float):
    return (-1.0) * (np.log(1.0 - y) / mu)

def main() -> None:

    # Variabili
    exp_events: list[float] = []
    x_min: float = 0.0
    x_max: float = 5.0

    # Parametri PDF
    mu: float = 1.5

    # Genera numeri esponenziali
    for i in range(10000):
        y = rand_range(x_min, x_max)
        exp_events.append(inverse_exponential_CDF(y, mu))

    # Plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 6")
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