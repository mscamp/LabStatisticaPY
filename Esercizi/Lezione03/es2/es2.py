"""
    ESERCIZIO 3.2
    Leggi il file eventi_unif.txt:
    * Stampa a schermo i primi 10 elementi positivi
    * Conta il numero di eventi nel file
    * Determina il valore massimo e il valore minimo
"""

# Librerie 
import numpy as np

def main():
    
    # Lettura del file di testo, che viene immesso in un array numpy
    path = "/home/scampo/Documents/Università/II anno/I semestre/Laboratorio di statistica/Python/Esercizi/Lezione03/es2/eventi_unif.txt"
    sample = np.loadtxt(path)

    # Stampa i primi 10 elementi positivi a schermo
    count = 0

    for element in sample:
        if element > 0 and count < 10:
            count += 1
            print(element)

        elif count >= 10:
            break

    # Numero di eventi
    print("Numero degli eventi: " + str(len(sample)))

    # Minimo e massimo valore
    minimo = np.min(sample)
    massimo = np.max(sample)

    print("Minimo: " + str(minimo))
    print("Massimo: " + str(massimo))

    return

if __name__ == "__main__":
    main()