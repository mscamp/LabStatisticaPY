# Librerie
import numpy as np

def median(array):
    """ Dato un array in input, lo ordina con np.sort() e restituisce la mediana """
    
    # Variabili
    sorted_array = np.sort(array)

    # Se len(array) è dispari, restituisce l'elemento centrale dell'array
    if (len(sorted_array) % 2 != 0):
        return (sorted_array[int(np.floor(len(sorted_array)/2))])

    # Se len(array) è pari, restituisce la media tra i due elementi centrali dell'array
    else:
        return (0.5 *(sorted_array[int(np.floor(len(sorted_array)/2))] + sorted_array[int(np.floor(len(sorted_array)/2)) - 1]))