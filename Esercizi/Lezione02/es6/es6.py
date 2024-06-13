""" 
    ESERCIZIO 2.6
    Dato un array di numeri, scrivi una libreria di Python che contenga una funzione che determini il valore
    al di sotto del quale si trova il 25% dei valori, e quello al di sopra del quale si trova il 25% dei valori
    Generalizza poi la funzione al caso in cui la percentuale dei valori nelle code si possa passare come
    argomento della funzione.
"""

# Librerie
import numpy as np
import percentile_lib as pl

def main():

    # Variabili
    arr = np.array([1.235, 51.34, 72.23535, 2823.34, 324.5646, 123.164634, 235.2634, 543.26, 24.457, 424.4574, 414.236346, 122.2353, 49.45364, 84.152, 37.36225, 39.256342, 645.26])
    print(np.sort(arr))

    # Percentile 25
    print("Valore al di sotto del quale 25%: " + str(pl.percentile25_low(arr)))

    # Percentile 75
    print("Valore al di sopra del quale 25%: " + str(pl.percentile25_high(arr)))

    # Percentile generico
    print("Valore al di sotto del quale 37%: " + str(pl.percentile(arr, 0.37)))

    return

if __name__ == "__main__":
    main()
