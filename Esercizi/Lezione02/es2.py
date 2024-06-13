""" 
    ESERCIZIO 2.2
    Crea un array 1-dimensionale di NumPy contenente una successione di interi da 1 a 100, poi crea a partire
    da questo un array NumPy che contiene in ciascuna entrata la somma degli interi da 1 fino all'indice di 
    quell'entrata
"""

# Librerie
import numpy as np 

def main():

    # Variabili
    array = np.arange(1,101)
    array_cumsum = np.cumsum(array)

    # Stampa a schermo
    print(array_cumsum)

    return

if __name__ == "__main__":
    main()
