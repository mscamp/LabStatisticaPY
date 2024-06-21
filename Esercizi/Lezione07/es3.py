"""
    ESERCIZIO 7.3
    Usa il codice sorgente dell'esercizio precedente per aggiungere alla libreria usata nell'esercizio 1 una funzione che generi numeri pseudo-casuali distribuiti
    secondo Poisson, con la media passata come parametro:
    * Riscrivi l'esercizio precedente impiegando questa funzione, rappresentando anche la distribuzione in un istogramma
    * Calcola le statistiche del campione (media, varianza, skewness, kurtosi) usando una libreria
"""

# Librerie
from random_methods import *
from matplotlib import pyplot as plt
from stats import Stats
import scienceplots

def main() -> None:

    # Variabili
    N_experiments: int = 100000
    mu: float = 1.0
    t_M: float = 10.0
    sample_poiss: list[float] = gen_poisson(mu, t_M, N_experiments)

    # Statistiche del campione
    sample_poiss_stats = Stats(sample_poiss)

    media = sample_poiss_stats.mean()
    var = sample_poiss_stats.var()
    skew = sample_poiss_stats.skew()
    kurt = sample_poiss_stats.kurt()

    print(f"Media: {media}")
    print(f"Varianza: {var}")
    print(f"Skewness: {skew}")
    print(f"Kurtosi: {kurt}")

    # Plot
    plt.style.use(["science", "notebook"])
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 3", fontsize = 15, y = 1.03)
    ax.set_xlabel("Eventi poisson", fontsize = 8)
    ax.set_ylabel("Numero di eventi per bin", fontsize = 8)

    # Istogramma 
    x_min: float = max(0.0, np.ceil(np.mean(sample_poiss) - 3.0 * np.std(sample_poiss)))
    x_max: float = np.ceil(np.mean(sample_poiss) + 3.0 * np.std(sample_poiss))
    n_bins: int = int(np.floor(len(sample_poiss) / 100.0))
    bin_edges = np.linspace(x_min, x_max, n_bins)

    ax.hist(sample_poiss, bin_edges, color = "blue", label = "pmf(x)", histtype = "step", density = True)

    ax.legend(fontsize = 10)
    plt.savefig("es3.png")

    return

if __name__ == "__main__":
    main()