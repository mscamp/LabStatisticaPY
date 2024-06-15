"""
    ESERCIZIO 3.5
    Leggi il file di testo eventi_unif.txt e calcola:
    * La media
    * La varianza
    * La deviazione standard
    * La deviazione standard della media
"""

# Librerie
import numpy as np

def main():

    # Lettura del file di testo
    path = "/home/scampo/Documents/Università/II anno/I semestre/Laboratorio di statistica/Python/Esercizi/Lezione03/es5/eventi_unif.txt"
    sample = np.loadtxt(path)

    # Calcolo dei valori richiesti
    media = np.mean(sample)
    varianza = np.var(sample)
    devstd = np.std(sample)
    devstd_media = np.std(sample) / np.sqrt(len(sample))

    # Stampa a schermo
    print("Media: " + str(media))
    print("Varianza: " + str(varianza))
    print("Deviazione standard: " + str(devstd))
    print("Deviazione standard della media: " + str(devstd_media))

    return

if __name__ == "__main__":
    main()