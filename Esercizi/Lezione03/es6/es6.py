"""
    ESERCIZIO 3.6
    Scrivi una libreria di Python che, dato in input il nome di un file di testo contenente un campione di eventi, lo legga e salvi il suo contenuto all'interno di
    un array numpy, poi ne calcoli la media, la varianza, la deviazione standard, la deviazione standard della media e rappresenti il campione come istogramma, con
    un intervallo di definizione e un numero di bin opportunamente definiti. Scrivi poi un programma di test per la libreria creata.
"""

# Librerie
import istogramma as hg

def main():

    # Variabili
    path = "/home/scampo/Documents/Università/II anno/I semestre/Laboratorio di statistica/Python/Esercizi/Lezione03/es6/eventi_gauss.txt"
    stats = hg.statistiche(path)

    # Stampa a schermo le statistiche
    print(f"Media: {stats[0]}")
    print(f"Varianza: {stats[1]}")
    print(f"Deviazione standard: {stats[2]}")
    print(f"Deviazione standard della media: {stats[3]}")
    
    # Crea istogramma
    hg.crea_istogramma(path)

    return

if __name__ == "__main__":
    main()