"""
    ESERCIZIO 2.7
    Scrivi una libreria di Python che contenga funzioni che eseguano le seguenti operazioni su array
    * Calcola la media degli elementi
    * Calcola la varianza degli elementi
    * Calcola la deviazione standard degli elementi
    * Calcola la deviazione standard della media degli elementi
"""

# Librerie
import numpy as np
import statistica as st
import statistics

def main():

    # Variabili
    arr = np.array([2,5,6,2,6,3,5,3,6,8,1,2,3,9,10,2,3,5,2,6,23,4,75,371,82,1])
    lista = [2,5,6,2,6,3,5,3,6,8,1,2,3,9,10,2,3,5,2,6,23,4,75,371,82,1]

    # Media
    print("Media: " + str(st.media(arr)))

    # Varianza
    print("Varianza: " + str(st.varianza(arr)))

    # Deviazione standard
    print("Deviazione standard: " + str(st.devstd(arr)))

    # Deviazione standard della media
    print("Deviazione standard della media: " + str(st.devstd_media(arr)))

    return

if __name__ == "__main__":
    main()