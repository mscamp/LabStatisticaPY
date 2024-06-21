"""
    ESERCIZIO 7.2
    Utilizza il risultato dell'esercizio precedente per simulare un esperimento di conteggio poissoniano:
    * Scegli un tempo caratteristico t_0 per il processo
    * Scegli un tempo di misurazione t_M
    * Usando un loop, simula N pseudo-esperimenti di conteggio, in cui, per ciascuno di essi, una sequenza di numeri pseudo-casuali viene generata con intervalli di
    tempo caratteristici di un fenomeno poissoniano, finché il tempo passato non supera t_M, e conta quanti eventi cadono nel dato intervallo di tempo
    * Riempi un istogramma con i conteggi
"""

# Librerie
from random_methods import *
from matplotlib import pyplot as plt
import scienceplots

def main() -> None:

    # Variabili
    N_experiments: int = 100000
    t_0: float = 5.0
    t_M: float = 20.0
    sample_poiss: list[float] = []

    # Toy experiment
    for i in range(N_experiments):

        t:float = inverse_exponential_CDF(rand_range(0, 1), t_0)
        n_eventi: int = 0

        while t < t_M:
            n_eventi += 1
            t += inverse_exponential_CDF(rand_range(0, 1), t_0)

        sample_poiss.append(n_eventi)

    # Plot
    plt.style.use(["science", "notebook"])
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 2", fontsize = 15, y = 1.03)
    ax.set_xlabel("Eventi poisson", fontsize = 8)
    ax.set_ylabel("Numero di eventi per bin", fontsize = 8)

    # Istogramma 
    x_min: float = max(0.0, np.ceil(np.mean(sample_poiss) - 3.0 * np.std(sample_poiss)))
    x_max: float = np.ceil(np.mean(sample_poiss) + 3.0 * np.std(sample_poiss))
    n_bins: int = int(np.floor(len(sample_poiss) / 100.0))
    bin_edges = np.linspace(x_min, x_max, n_bins)

    ax.hist(sample_poiss, bin_edges, color = "blue", label = "pmf(x)", histtype = "step", density = True)

    ax.legend(fontsize = 10)
    plt.show()

    return

if __name__ == "__main__":
    main()