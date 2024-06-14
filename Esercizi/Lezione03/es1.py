"""
    ESERCIZIO 3.1
    Crea un istogramma monodimensionale riempito con 5 valori e salva l'immagine come file png
"""

# Librerie
import numpy as np
from matplotlib import pyplot as plt

def main():
    
    # Variabili
    sample = np.array([0.5, 2.1, 3.7, 1.1, 2.3])

    # Plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 1")
    ax.set_xlabel("Eventi")
    ax.set_ylabel("Numero eventi per bin")
    
    # Istogramma
    x_min = 0.0
    x_max = 4.0
    n_bins = 5
    bin_edges = np.linspace(x_min, x_max, n_bins)

    ax.hist(sample, bin_edges, color = "red")
    
    # Salva immagine
    path = "/home/scampo/Documents/Università/II anno/I semestre/Laboratorio di statistica/Python/Esercizi/Lezione03/plot.png"
    plt.savefig(path)

    return

if __name__ == "__main__":
    main()