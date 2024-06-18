"""
    ESERCIZIO 5.4
    Scrivi un programma che legga il file eventi_unif.txt e, usando la funzione filter(), crei due sottoinsiemi differenti di eventi,
    contenenti rispettivamente gli eventi minori e quelli maggiori della media, servendosi di lambda functions. Mostra inoltre che la
    deviazione standard degli eventi nei due sottoinsiemi è la metà del sample originale.
"""

# Librerie
import numpy as np

def main() -> None:

    # Variabili
    path: str = "/home/scampo/Documents/Università/II anno/I semestre/Laboratorio di statistica/Python/Esercizi/Lezione05/es4/eventi_unif.txt"
    sample = np.loadtxt(path)

    # Filtra i dati
    media: float = np.mean(sample)
    sigma: float = np.std(sample)
    lesser_than_mean = list(filter(lambda x : x < media, sample))
    greater_than_mean= list(filter(lambda x : x >= media, sample))
    sigma_lesser: float = np.std(lesser_than_mean)
    sigma_greater: float = np.std(greater_than_mean)

    # Stampa a schermo
    print(f"Media: {media}")
    print(f"Rapporto tra le sigma per i valori sotto la media: {sigma_lesser / sigma}")
    print(f"Rapporto tra le sigma per i valori sopra la media: {sigma_greater / sigma}")

    return

if __name__ == "__main__":
    main()