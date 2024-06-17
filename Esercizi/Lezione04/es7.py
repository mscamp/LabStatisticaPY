"""
    ESERCIZIO 4.7
    Implementa un generatore di numeri pseudo-casuali che sfrutti il teorema centrale del limite per generare eventi distribuiti 
    secondo una gaussiana.
    * Si può ottenere una gaussiana centrata in x = 0 con varianza unitaria?
    * Verifica che all'aumentare del numero di eventi, la distribuzione ottenuta tende ad una gaussiana, sia graficamente che usando
    i momenti della distribuzione e confrontandoli con i momenti del campione
"""

# Librerie
import numpy as np
from matplotlib import pyplot as plt
from random import random
from scipy.stats import norm, skew, kurtosis

def sturges(n_eventi: int) -> int:
    return int(np.ceil(1.0 + 3.322 * np.log(n_eventi)))

def rand_range(x_min: float, x_max: float) -> float:
    return x_min + (x_max - x_min) * random()

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

def main() -> None:

    # Variabili
    N: int = 10000
    x_min: float = -20.0
    x_max: float = 20.0
    media: float = 0.0
    sigma: float = 1.0
    sample: list[float] = gen_TCL_ms(media, sigma, N)

    # Funzione da plottare
    gauss_pdf = norm(media, sigma)
    x_coord = np.linspace(x_min, x_max, 100000)

    # Plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 7")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Istogramma
    n_bins: int = sturges(len(sample))
    bin_edges = np.linspace(x_min, x_max, n_bins)
    plt.hist(sample, bin_edges, color = "blue", label = "Campione", histtype = "step", density = True)
    plt.plot(x_coord, gauss_pdf.pdf(x_coord), color = "red", label = "pdf(x)")

    ax.legend()
    plt.savefig("confronto_grafico.png")

    # Confronto dei momenti
    gauss_mean, gauss_var, gauss_skew, gauss_kurt = gauss_pdf.stats(moments = "mvsk")
    scarti_media: list[float] = []
    scarti_var: list[float] = []
    scarti_skew: list[float] = []
    scarti_kurt: list[float] = []
    x_coord = np.arange(1, 100001, 1000)

    for i in range(1, 100001, 1000):
        sample: list[float] = gen_TCL_ms(media, sigma, i)

        scarti_media.append(np.abs(np.mean(sample) - gauss_mean))
        scarti_var.append(np.abs(np.var(sample) - gauss_var))
        scarti_skew.append(np.abs(skew(sample) - gauss_skew))
        scarti_kurt.append(np.abs(kurtosis(sample) - gauss_kurt))

    # Plot
    fig, axes = plt.subplots(nrows = 2, ncols = 2)
    plt.suptitle("Esercizio 7")

    axes[0][0].plot(x_coord, scarti_media, "-", color = "red", label = "scarti media")
    axes[0][1].plot(x_coord, scarti_var, "-", color = "green", label = "scarti varianza")
    axes[1][0].plot(x_coord, scarti_skew, "-", color = "blue", label = "scarti skewness")
    axes[1][1].plot(x_coord, scarti_kurt, "-", color = "orange", label = "scarti kurtosi")

    for i in range(2):
        for j in range(2):
            axes[i][j].set_xlabel("x")
            axes[i][j].set_ylabel("y")
            axes[i][j].legend()

    plt.savefig("scarti_momenti.png")

    return

if __name__ == "__main__":
    main()