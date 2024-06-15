# Librerie
import numpy as np
from matplotlib import pyplot as plt

def sturges(n_eventi):
    return int(np.ceil(1 + 3.322 * np.log(n_eventi)))

def statistiche(file_path):

    # Variabili
    sample = np.loadtxt(file_path)
    media = np.mean(sample)
    varianza = np.var(sample)
    devstd = np.std(sample)
    devstd_media = np.std(sample) / np.sqrt(len(sample))

    return [media, varianza, devstd, devstd_media]

def crea_istogramma(file_path):

    # Lettura file di testo
    sample = np.loadtxt(file_path)

    # Plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 6")
    ax.set_xlabel("Eventi")
    ax.set_ylabel("Numero di eventi per bin")

    # Parametri istogramma
    x_min = np.min(sample)
    x_max = np.max(sample)
    n_bin = sturges(len(sample))
    bin_edges = np.linspace(x_min, x_max, n_bin)

    # Istogramma
    ax.hist(sample, bin_edges, color = "blue")

    plt.show()

    return