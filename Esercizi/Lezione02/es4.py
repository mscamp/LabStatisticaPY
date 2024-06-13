""" 
    ESERCIZIO 2.4
    In un programma di Python, il tempo corrente può essere ottenuto attraverso la libreria time. Compara i
    tempi di esecuzione delle operazioni element-wise tra due liste con la stessa operazione tra due array
    NumPy. Dopo quale dimensione dei vettori la differenza inizia ad essere significativa?
"""

# Librerie
import numpy as np
import time

def pointwise_sum_lists(a, b):
    """ Prende in input due liste della stessa dimensione e restituisce il tempo necessario per sommarle """

    # Primo snapshot
    time_snapshot_in = time.time()

    # Variabili
    res = [a[i] + b[i] for i in range(0, len(a) - 1)] 

    # Secondo snapshot
    time_snapshot_fin = time.time()

    return (time_snapshot_fin - time_snapshot_in)

def pointwise_sum_arrays(a, b):
    """ Prende in input due ndarray della stessa dimensione e restituisce il tempo necessario per sommarli """

    # Primo snapshot
    time_snapshot_in = time.time()

    # Variabili
    res = a + b

    # Secondo snapshot
    time_snapshot_fin = time.time()

    return (time_snapshot_fin - time_snapshot_in)


def main():

    # Variabili
    dim = 1001
    list_a = range(1, dim)
    list_b = range(1, dim)
    array_a = np.arange(1, dim)
    array_b = np.arange(1, dim)
    time_lists = pointwise_sum_lists(list_a, list_b)
    time_arrays = pointwise_sum_arrays(array_a, array_b)
    delta = time_lists - time_arrays

    # Stampa a schermo
    print(f"Tempo per liste: {time_lists}")
    print(f"Tempo per array: {time_arrays}")
    print(f"Differenza: {delta}")

    return

if __name__ == "__main__":
    main()