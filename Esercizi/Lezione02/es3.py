""" 
    ESERCIZIO 2.3
    Crea un array contenente la successione dei primi 50 numeri pari
    Crea un array contenente la successione dei primi 50 numeri dispari
    Crea un array che deve essere la somma elemento per elemento dei due array creati in precedenza
"""

# Librerie
import numpy as np

def main():

    # Variabili
    array_pari = np.arange(2, 102, 2)
    array_dispari = np.arange(1, 101, 2)
    array_somma = array_pari + array_dispari
    
    # Stampa a schermo
    print(array_pari)
    print(array_dispari)
    print(array_somma)

    return

if __name__ == "__main__":
    main()