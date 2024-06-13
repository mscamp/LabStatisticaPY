""" 
    ESERCIZIO 2.5
    Usando numpy.sort(), scrivi una libreria di Python contenente una funzione che determina il valore mediano
    di un ndarray. Scrivi un programma per testare la funzione costruita.
"""

# Librerie
import numpy as np
import mediana

def main():

    # Variabili
    array = np.array([3, 2, 1, 57, 48, 74, 22, 21, 20, 88, 32])
    md = mediana.median(array)

    # Stampa a schermo
    print(f"Mediana: {md}")

    return

if __name__ == "__main__":
    main()