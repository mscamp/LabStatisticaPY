# Librerie
from random_methods import *

def hit_or_miss(f, a: float, b: float, y_max: float, N: int) -> list[float]:

    # Variabili
    n_hit: int = 0
    A: float = y_max * np.abs(b - a)

    # Loop sul numero di punti
    for i in range(N):
        x = rand_range(a, b)
        y = rand_range(0.0, y_max)

        if y < f(x):
            n_hit += 1

    p: float = (n_hit / N)
    integral: float = p * A
    error: float = (A / np.sqrt(N)) * p * (1.0 - p)

    return [integral, error]

def crude_MC(f, a: float, b: float, N: int):

    # Variabili
    x_i: list[float] = gen_unif(a, b, N)
    f_x_i: list[float] = list(map(f, x_i))

    # Calcolo integrale
    integral: float = (b - a) * np.mean(f_x_i)
    error: float = (b - a) * (np.std(f_x_i) / np.sqrt(N))

    return [integral, error]