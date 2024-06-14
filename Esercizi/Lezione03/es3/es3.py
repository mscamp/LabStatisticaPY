"""
    ESERCIZIO 3.3
    * Riempi un istogramma con i primi N valori contenuti nel file eventi_gauss.txt, dove N è un parametro passato da riga di comando
    * Fai in modo che l'intervallo di definizione dell'istogramma e il numero dei bin dipenda dai valori che si devono rappresentare
"""

# Librerie
import sys
import numpy as np
from matplotlib import pyplot as plt

def sturges(n_eventi):
    return int(np.ceil(1 + 3.322 * np.log(n_eventi)))

def main():

    # Controllo argomenti passati da riga di comando
    if len(sys.argv) != 2:
        print("Utilizzo: python3 es3.py n_eventi")
        exit(1)

    N = int(sys.argv[1])

    # Lettura del file di testo
    path = "/home/scampo/Documents/Università/II anno/I semestre/Laboratorio di statistica/Python/Esercizi/Lezione03/es3/eventi_gauss.txt"
    sample_list = []

    i = 0 # counter

    with open(path) as input_file:
        for line in input_file.readlines():
            sample_list.append(float(line))

            i += 1

            if i >= N:
                break
             
    # Campione
    sample = np.array(sample_list)

    # Parametri istogramma
    x_min = np.min(sample)
    x_max = np.max(sample)
    n_bins = sturges(N)

    # Plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)

    # Styling
    ax.set_title("Esercizio 3")
    ax.set_xlabel("Eventi gaussiani")
    ax.set_ylabel("Numero di eventi per bin")

    # Istogramma
    bin_edges = np.linspace(x_min, x_max, n_bins)
    ax.hist(sample, bin_edges, color = "violet", histtype = "step")

    plt.show()

    return

if __name__ == "__main__":
    main()

    