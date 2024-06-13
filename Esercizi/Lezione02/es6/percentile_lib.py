# Librerie
import numpy as np

def percentile25_low(array):
    """ Determina il valore al di sotto del quale si trova il 25% dei valori """
    sorted_array = np.sort(array)
    index = int(0.25 * len(array))

    return sorted_array[index]

def percentile25_high(array):
    """ Determina il valore al di sopra del quale si trova il 25% dei valori """
    sorted_array = np.sort(array)
    index = int(0.75 * len(array))

    return sorted_array[index]

def percentile(array, percentage):
    """ Determina il valore al di sotto del quale si trova il percentage% dei valori """
    sorted_array = np.sort(array)
    index = int(percentage * len(array))

    return sorted_array[index]