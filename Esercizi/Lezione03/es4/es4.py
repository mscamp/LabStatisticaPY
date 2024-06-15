"""
    ESERCIZIO 3.4
    Mostra le distribuzioni di eventi dei due esercizi precedenti sovrapposte, cercando il metodo migliore di visualizzazione che
    consenta un confronto tra i due istogrammi
"""

# Libreria
import numpy as np
from matplotlib import pyplot as plt

def sturges(n_eventi):
    return int(np.ceil(1 + 3.322 * np.log(n_eventi)))

def main():
    
    # Path dei file
    path_unif = "/home/scampo/Documents/Università/II anno/I semestre/Laboratorio di statistica/Python/Esercizi/Lezione03/es4/eventi_unif.txt"
    path_gauss = "/home/scampo/Documents/Università/II anno/I semestre/Laboratorio di statistica/Python/Esercizi/Lezione03/es4/eventi_gauss.txt"

    # Lettura dei file
    sample_unif = np.loadtxt(path_unif)
    sample_gauss = np.loadtxt(path_gauss)

    # Parametri istogramma
    x_min = np.floor(min(np.min(sample_unif), np.min(sample_gauss)))
    x_max = np.ceil(min(np.max(sample_unif), np.max(sample_gauss)))
    n_bins = sturges(min(len(sample_unif), len(sample_gauss)))
    bin_edges = np.linspace(x_min, x_max, n_bins)

    # Plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 4")
    ax.set_xlabel("Eventi")
    ax.set_ylabel("Numero di eventi per bin")

    # Istogrammi 
    ax.hist(sample_unif, bin_edges, color = "blue", histtype = "step")
    ax.hist(sample_gauss, bin_edges, color = "red", histtype = "step")

    plt.show()

    return

if __name__ == "__main__":
    main()