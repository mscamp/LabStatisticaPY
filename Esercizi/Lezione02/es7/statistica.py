# Librerie
import numpy as np
import math

def media(array):
    """ Restituisce la media di un array """
    return (np.sum(array) / len(array))

def varianza(array, bessel=True):
    """ Restituisce la varianza di un array """
    
    # Variabili
    m = media(array)
    scarti = array - m

    if bessel:
        return np.sum(scarti**2) / (len(array) - 1)
    
    else:
        return np.sum(scarti**2) / len(array)

def devstd(array, bessel=True):
    """ Restituisce la deviazione standard di un array con/senza correzione di Bessel """

    # Variabili
    m = media(array)
    scarti = array - m

    if bessel:
        return np.sqrt(np.sum(scarti**2) / (len(array) - 1))

    else:
        return np.sqrt(np.sum(scarti**2) / (len(array)))

def devstd_media(array, bessel=True):
    """ Restituisce la deviazione standard della media di un array con/senza correzione di Bessel """
    
    return devstd(array, bessel) / np.sqrt(len(array))