"""
    ESERCIZIO 7.1
    Genera un campione di numeri pseudo-casuali distribuiti secondo un'esponenziale con tempo caratteristico
    t_0 di 5 secondi, poi:
    * Rappresenta graficamente la distribuzione usando un istogramma
    * Scrivi le funzioni per generare i numeri pseudo-casuali in una libreria esterna al programma
"""

# Librerie
from random_methods import *
from matplotlib import pyplot as plt
import scienceplots

def main() -> None:

    # Variabili
    N: int = 100000
    x_min: float = 0.0
    x_max: float = 50.0
    t_0: float = 5.0
    sample_exp = gen_inverse_exponential_CDF(t_0, N)

    # Plot
    plt.style.use(["science", "notebook"])
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 1", fontsize = 15, y = 1.03)
    ax.set_xlabel("Eventi exp", fontsize = 8)
    ax.set_ylabel("Numero di eventi per bin", fontsize = 8)

    # Istogramma 
    n_bins: int = sturges(len(sample_exp))
    bin_edges = np.linspace(x_min, x_max, n_bins)

    ax.hist(sample_exp, bin_edges, color = "green", label = "pdf(x)", histtype = "step", density = True)

    ax.legend(fontsize = 10)
    plt.show()

    return

if __name__ == "__main__":
    main()