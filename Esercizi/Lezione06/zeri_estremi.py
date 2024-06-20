# Librerie
import numpy as np

def bisezione(g, x_min: float, x_max: float, precision: float = 0.0001) -> float:
    """ Calcola lo zero di una funzione in un dato intervallo usando il metodo di bisezione """

    # Controllo argomenti passati
    if (x_max - x_min) <= 0:
        raise ValueError("x_max deve essere strettamente maggiore di x_min")

    if precision <= 0:
        raise ValueError("La precisione deve essere strettamente maggiore di zero")

    # Caso banale
    if g(x_min) == 0:
        return x_min

    elif g(x_max) == 0:
        return x_max

    # Algoritmo
    x_mean: float = x_min 

    while (x_max - x_min) > precision:
        x_mean: float = 0.5 * (x_max + x_min)

        if g(x_mean) * g(x_min) > 0.0:
            x_min: float = x_mean
        
        else:
            x_max: float = x_mean

    return x_mean

def bisezione_ricorsiva(g, x_min: float, x_max: float, precision: float = 0.0001) -> float:
    """ Calcola lo zero di una funzione in un dato intervallo usando il metodo di bisezione """
    
    # Controllo argomenti passati
    if (x_max - x_min) <= 0:
        raise ValueError("x_max deve essere strettamente maggiore di x_min")

    if precision <= 0:
        raise ValueError("La precisione deve essere strettamente maggiore di zero")

    # Caso banale
    if g(x_min) == 0:
        return x_min

    elif g(x_max) == 0:
        return x_max

    x_mean: float = 0.5 * (x_max + x_min)

    # Condizione di arresto
    if (x_max - x_min) < precision:
        return x_mean

    # Algoritmo
    if g(x_mean) * g(x_min) > 0.0:
        return bisezione_ricorsiva(g, x_mean, x_max, precision)

    else:
        return bisezione_ricorsiva(g, x_min, x_mean, precision)

def find_min(g, x_min: float, x_max: float, precision: float = 0.0001) -> float:
    """ Determina il minimo di una funzione in un dato intervallo usando il metodo della sezione aurea """

    # Controllo argomenti passati
    if (x_max - x_min) <= 0:
        raise ValueError("x_max deve essere strettamente maggiore di x_min")

    if precision <= 0:
        raise ValueError("La precisione deve essere strettamente maggiore di zero")

    phi: float = 0.5 * (np.sqrt(5.0) - 1.0)

    while (x_max - x_min) > precision:
        x_2: float = x_min + (1.0 - phi) * (x_max - x_min)
        x_3: float = x_min + phi * (x_max - x_min)

        if g(x_3) < g(x_2):
            x_min: float = x_2

        else:
            x_max: float = x_3

    return 0.5 * (x_min + x_max)

def find_max(g, x_min: float, x_max: float, precision: float = 0.0001) -> float:
    """ Determina il massimo di una funzione in un dato intervallo usando il metodo della sezione aurea """

    # Controllo argomenti passati
    if (x_max - x_min) <= 0:
        raise ValueError("x_max deve essere strettamente maggiore di x_min")

    if precision <= 0:
        raise ValueError("La precisione deve essere strettamente maggiore di zero")

    phi: float = 0.5 * (np.sqrt(5.0) - 1.0)

    while (x_max - x_min) > precision:
        x_2: float = x_min + (1.0 - phi) * (x_max - x_min)
        x_3: float = x_min + phi * (x_max - x_min)

        if g(x_3) > g(x_2):
            x_min: float = x_2

        else:
            x_max: float = x_3

    return 0.5 * (x_min + x_max)

def find_min_recursive(g, x_min: float, x_max: float, precision: float = 0.0001):

    # Controllo argomenti passati
    if (x_max - x_min) <= 0:
        raise ValueError("x_max deve essere strettamente maggiore di x_min")

    if precision <= 0:
        raise ValueError("La precisione deve essere strettamente maggiore di zero")

    phi: float = 0.5 * (np.sqrt(5.0) - 1.0)
    x_2: float = x_min + (1.0 - phi) * (x_max - x_min)
    x_3: float = x_min + phi * (x_max - x_min)

    if (x_max - x_min) < precision:
        return 0.5 * (x_max + x_min)

    elif g(x_3) < g(x_2):
        x_min = x_2
        return find_min_recursive(g, x_min, x_max)

    else:
        x_max = x_3
        return find_min_recursive(g, x_min, x_max)

def find_max_recursive(g, x_min: float, x_max: float, precision: float = 0.0001):

    # Controllo argomenti passati
    if (x_max - x_min) <= 0:
        raise ValueError("x_max deve essere strettamente maggiore di x_min")

    if precision <= 0:
        raise ValueError("La precisione deve essere strettamente maggiore di zero")

    phi: float = 0.5 * (np.sqrt(5.0) - 1.0)
    x_2: float = x_min + (1.0 - phi) * (x_max - x_min)
    x_3: float = x_min + phi * (x_max - x_min)

    if (x_max - x_min) < precision:
        return 0.5 * (x_max + x_min)

    elif g(x_3) > g(x_2):
        x_min = x_2
        return find_max_recursive(g, x_min, x_max)

    else:
        x_max = x_3
        return find_max_recursive(g, x_min, x_max)