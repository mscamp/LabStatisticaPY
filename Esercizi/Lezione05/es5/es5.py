"""
    ESERCIZIO 5.5
    Scrivi un programma di Python che legga il file eventi_gauss.txt e, usando la funzione map(), crei la distribuzione dei quadrati e
    dei cubi del sample originale, servendosi di lambda functions. Plotta le tre distribuzioni sovrapposte.
"""

# Librerie
import numpy as np
from matplotlib import pyplot as plt

def sturges(n_eventi):
    return int(np.ceil(1.0 + 3.322 * np.log(n_eventi)))

def main() -> None:

    # Legge il file di testo
    path: str = "/home/scampo/Documents/Università/II anno/I semestre/Laboratorio di statistica/Python/Esercizi/Lezione05/es5/eventi_gauss.txt"
    sample = np.loadtxt(path)
    
    # Genera le distribuzioni dei quadrati e dei cubi
    sample_squared = list(map(lambda x : x**2, sample))
    sample_cubed = list(map(lambda x : x**3, sample))

    # Istogrammi
    x_min = -5.0
    x_max = 5.0
    n_bins = sturges(len(sample))
    bin_edges = np.linspace(x_min, x_max, n_bins)

    # Plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 5")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    
    ax.hist(sample, bin_edges, color = "orange", label = "sample", histtype = "step", density = True)
    ax.hist(sample_squared, bin_edges, color = "red", label = "sample squared", histtype = "step", density = True)
    ax.hist(sample_cubed, bin_edges, color = "green", label = "sample cubed", histtype = "step", density = True)

    ax.legend()
    plt.show()

    return

if __name__ == "__main__":
    main()