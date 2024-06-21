"""
    ESERCIZIO 8.1
    Scrivi un programma che, dato un numero N_max, genera N_toys toy experiment, ciascuno contenente un campione di N_max eventi 
    distribuiti secondo una data distribuzione, e calcola la loro media

    ESERCIZIO 8.2
    Aggiungi al programma un istogramma che rappresenti la distribuzione della media

    ESERCIZIO 8.3
    Usa la classe "stats" per confrontare la deviazione standard della media calcolata per ciascun toy experiment con la deviazione 
    standard del campione delle medie

    ESERCIZIO 8.4
    Utilizza due scatter plot per confrontare l'evoluzione della deviazione standard della media calcolata per ogni toy con la deviazione
    standard del campione delle medie in funzione del numero di eventi generati in un singolo toy experiment

"""

# Librerie
import numpy as np
from random_methods import gen_unif, sturges
from stats import Stats
from matplotlib import pyplot as plt
import scienceplots

def main() -> None:

    # Variabili
    x_min: float = 0.0
    x_max: float = 10.0
    N_max: int = 10000
    N_toys: int = 10000

    sample_of_means: list[float] = []
    sample_of_std_means: list[float] = [] # es 3
    
    # Loop sui toy experiment (es 1)
    for i in range(N_toys):
        sample: list[float] = gen_unif(x_min, x_max, N_max)
        sample_stats = Stats(sample)
        sample_of_means.append(sample_stats.mean())
        sample_of_std_means.append(sample_stats.std_mean()) # es 3

    # Confronto tra deviazione standard della media e deviazione standard del campione delle medie (es 3)
    sample_of_means_stats = Stats(sample_of_means)
    sample_of_std_means_stats = Stats(sample_of_std_means)

    scarto: float= np.abs(sample_of_std_means_stats.mean() - sample_of_means_stats.std())
    print(f"Scarto tra le std mean: {scarto}")

    # Plot (es 2)
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 2")
    ax.set_xlabel("Media campionaria")
    ax.set_ylabel("Distribuzione della media")

    # Istogramma
    x_min_hist: float = 4.75
    x_max_hist: float = 5.25
    n_bins = sturges(len(sample_of_means))
    bin_edges = np.linspace(x_min_hist, x_max_hist, n_bins)

    ax.hist(sample_of_means, bin_edges, color = "orange", label = "Distribuzione della media", density = True)

    plt.savefig("es2.png")

    # Esercizio 4
    y_1: list[float] = []
    y_2: list[float] = []
    x_coord = np.arange(2, N_max + 2)

    for i in range(N_toys):

        sample_of_means: list[float] = []
        sample_of_std_means: list[float] = []

        for j in range(2, N_max + 2):
            sample: list[float] = gen_unif(x_min, x_max, j)
            sample_stats = Stats(sample)
            sample_of_means.append(sample_stats.mean())
            sample_of_std_means.append(sample_stats.std_mean()) 
            sample_of_means_stats = Stats(sample_of_means)
            sample_of_std_means_stats = Stats(sample_of_std_means)

        y_1.append(sample_of_means_stats.std()) 
        y_2.append(sample_of_std_means_stats.mean()) 

    # Plot (es 4)
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 4")
    ax.set_xlabel("N eventi per toy")
    ax.set_ylabel("y")

    ax.plot(x_coord, y_1, "-", color = "red", label = "Dev standard delle medie")
    ax.plot(x_coord, y_2, "-", color = "blue", label = "Media delle devstd della media")

    ax.legend()
    plt.savefig("es4.png")

    return

if __name__ == "__main__":
    main()