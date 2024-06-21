"""
    ESERCIZIO 7.4
    Usa il risultato dell'esercizio precedente per calcolare le statistiche di una distribuzione di Poisson, variando la media da 1 a
    250 (come si deve campionare l'intervallo?). Plotta la skewness e la kurtosi in funzione della media della distribuzione.
"""

# Librerie
from random_methods import *
from matplotlib import pyplot as plt
from stats import Stats
import scienceplots

def main() -> None:

    # Variabili
    N_experiments: int = 1000
    mu: float = 1.0

    # Plot
    plt.style.use(["science", "notebook", "grid"])
    fig, axes = plt.subplots(nrows = 1, ncols = 2)
    fig.suptitle("Esercizio 4", y = 0.87, fontsize = 20)
    fig.tight_layout(pad = 3)
    fig.text(0.5, 0.05, "Media", ha = "center", size = 15)
    axes[0].set_ylabel("Skewness", fontsize = 10)
    axes[1].set_ylabel("Kurtosi", fontsize = 10)

    # Ciclo sulla media    
    media_list: list[float] = []
    skew_list: list[float] = []
    kurt_list: list[float] = []

    for i in range(1, 251):
        sample_poiss: list[float] = gen_poisson(mu, i, N_experiments)
        sample_poiss_stats = Stats(sample_poiss)

        media_list.append(sample_poiss_stats.mean())
        skew_list.append(sample_poiss_stats.skew())
        kurt_list.append(sample_poiss_stats.kurt())

    # Plot
    axes[0].plot(media_list, skew_list, "-", color = "blue", label = "Skewness")
    axes[1].plot(media_list, kurt_list, "-", color = "blue", label = "Kurtosi")

    axes[0].legend()
    axes[1].legend()

    plt.savefig("es4.png")

    return

if __name__ == "__main__":
    main()