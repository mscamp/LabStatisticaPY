# Librerie
import numpy as np
from random import random

def sturges(n_eventi: int) -> int:
    return int(np.ceil(1.0 + 3.322 * np.log(n_eventi)))

def rand_range(x_min: float, x_max: float) -> float:
    return x_min + (x_max - x_min) * random()

def gen_unif(x_min: float, x_max: float, N: int) -> list[float]:
    
    sample: list[float] = []

    for i in range(N):
        sample.append(rand_range(x_min, x_max))

    return sample

def rand_TAC(f, x_min: float, x_max: float, y_max: float) -> float:

    x = rand_range(x_min, x_max)
    y = rand_range(0, y_max)

    while y > f(x):
        x = rand_range(x_min, x_max)
        y = rand_range(0, y_max)

    return x

def gen_TAC(f, x_min: float, x_max: float, y_max: float, N: int) -> list[float]:

    sample: list[float] = []

    for i in range(N):
        sample.append(rand_TAC(f, x_min, x_max, y_max))

    return sample

def inverse_exponential_CDF(y: float, t_0: float) -> float: # y con distribuzione uniforme tra 0 e 1

    if t_0 == 0:
        raise ZeroDivisionError("t_0 deve essere diverso da zero")

    mu = 1.0 / t_0

    return (-1.0) * (np.log(1.0 - y) / mu)

def gen_inverse_exponential_CDF(t_0: float, N: int) -> list[float]:

    sample: list[float] = []

    for i in range(N):
        y = rand_range(0, 1)
        sample.append(inverse_exponential_CDF(y, t_0))

    return sample

def gen_poisson(mu: float, t_M: float, N: int) -> list[float]:

    t_0 = 1.0 / mu
    sample: list[float] = []

    for i in range(N):

        t:float = inverse_exponential_CDF(rand_range(0, 1), t_0)
        n_eventi: int = 0

        while t < t_M:
            n_eventi += 1
            t += inverse_exponential_CDF(rand_range(0, 1), t_0)

        sample.append(n_eventi)
    
    return sample

def rand_TCL(N_sum: int, x_min: float, x_max: float) -> float:

    # Variabili
    sample: list[float] = []

    for i in range(N_sum):
        sample.append(rand_range(x_min, x_max))
    
    return sum(sample) / len(sample)

def gen_TCL(x_min: float, x_max: float, N: int, N_sum: int = 10) -> list[float]:

    # Variabili
    gauss_events: list[float] = []

    for i in range(N):
        gauss_events.append(rand_TCL(N_sum, x_min, x_max))
    
    return gauss_events

def rand_TCL_ms(N_sum: int, media: float, sigma: float) -> float:

    # Variabili
    sample: list[float] = []
    delta = np.sqrt(3 * N_sum) * sigma
    x_min = media - delta
    x_max = media + delta

    for i in range(N_sum):
        sample.append(rand_range(x_min, x_max))
    
    return sum(sample) / len(sample)

def gen_TCL_ms(media: float, sigma: float, N: int, N_sum: int = 10) -> list[float]:

    # Variabili
    gauss_events: list[float] = []

    for i in range(N):
        gauss_events.append(rand_TCL_ms(N_sum, media, sigma))
    
    return gauss_events
