# Librerie
import numpy as np

def loglikelihood(f, sample: list[float], par: float) -> float:

    sum: float = 0.0

    for i in range(len(sample)):
        if f(sample[i], par) > 0.0:
            sum += np.log(f(sample[i], par))

    return sum

def find_max_likelihood(g, pdf, sample: list[float], x_min: float, x_max: float, precision: float = 0.0001) -> float: 

    # Controllo argomenti passati
    if (x_max - x_min) <= 0:
        raise ValueError("x_max deve essere strettamente maggiore di x_min")

    if precision <= 0:
        raise ValueError("La precisione deve essere strettamente maggiore di zero")

    phi: float = 0.5 * (np.sqrt(5.0) - 1.0)

    while (x_max - x_min) > precision:
        x_2: float = x_min + (1.0 - phi) * (x_max - x_min)
        x_3: float = x_min + phi * (x_max - x_min)

        if g(pdf, sample, x_3) > g(pdf, sample, x_2):
            x_min: float = x_2

        else:
            x_max: float = x_3

    return 0.5 * (x_min + x_max)

def h(pdf, sample: list[float], par: float, par_max: float) -> float:
    return (loglikelihood(pdf, sample, par) - loglikelihood(pdf, sample, par_max) + 0.5)

def bisezione_h(g, pdf, sample: list[float], x_min: float, x_max: float, par_max: float, precision: float = 0.0001) -> float:

    # Controllo argomenti passati
    if (x_max - x_min) <= 0:
        raise ValueError("x_max deve essere strettamente maggiore di x_min")

    if precision <= 0:
        raise ValueError("La precisione deve essere strettamente maggiore di zero")

    # Caso banale
    if g(pdf, sample, x_min, par_max) == 0:
        return x_min

    elif g(pdf, sample, x_max, par_max) == 0:
        return x_max

    # Algoritmo
    x_mean: float = x_min 

    while (x_max - x_min) > precision:
        x_mean: float = 0.5 * (x_max + x_min)

        if g(pdf, sample, x_mean, par_max) * g(pdf, sample, x_min, par_max) > 0.0:
            x_min: float = x_mean
        
        else:
            x_max: float = x_mean

    return x_mean