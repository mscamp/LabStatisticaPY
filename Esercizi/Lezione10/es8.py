"""
    ESERCIZIO 10.8
    In regime asintotico (per N grande), la distribuzione degli scarti (t_0 - t_0_true) / sigma_t_0 segue una
    distribuzione gaussiana:
    * Usa la tecnica dei toy experiment per riempire un istogramma con gli scarti
    * Calcola la media e la deviazione standard della distribuzione delle differenze e plotta i loro valori
    in funzione del numero di eventi usati per la stima
"""

# Librerie
from random_methods import *
from max_likelihood import *
from matplotlib import pyplot as plt
import scienceplots

def exp_pdf(x: float, t_0: float) -> float:
    return (1.0 / t_0) * np.exp((-1.0) * (x / t_0))

def main() -> None:

    # Variabili
    t_0: float = 1.5
    N: int = 100
    N_toys: int = 1000
    scarti: list[float] = []
    x_min: float = 0.5
    x_max: float = 2.0
    
    # Parte 1
    # Loop sui toys
    for i in range(N_toys):

        sample_exp: list[float] = gen_inverse_exponential_CDF(t_0, N)
        par_max: float = find_max_likelihood(loglikelihood, exp_pdf, sample_exp, x_min, x_max)

        y_intersection_1: float = bisezione_h(h, exp_pdf, sample_exp, x_min, t_0, par_max)
        y_intersection_2: float = bisezione_h(h, exp_pdf, sample_exp, t_0, x_max, par_max)

        sigma_ML: float = 0.5 * (y_intersection_2 - y_intersection_1)

        scarto: float = (par_max - t_0) / sigma_ML

        scarti.append(scarto)

    # Plot
    plt.style.use(["science", "notebook"])
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 8 parte 1")
    ax.set_xlabel("t_0")
    ax.set_ylabel("Eventi per bin")

    # Istogramma
    x_min_hist: float = -1.5
    x_max_hist: float = 1.5
    n_bins: int = sturges(len(scarti))
    bin_edges = np.linspace(x_min_hist, x_max_hist, n_bins)

    ax.hist(scarti, bin_edges, color = "orange", label = "Distribuzione degli scarti", density = True)

    ax.legend(loc = "lower right", fontsize = 10)
    plt.savefig("es8_1.png")

    # Parte 2
    scarti_means: list[float] = []
    scarti_devstd: list[float] = []

    for i in range(N):

        scarti: list[float] = []

        for j in range(N_toys):
            sample_exp: list[float] = gen_inverse_exponential_CDF(t_0, i)
            par_max: float = find_max_likelihood(loglikelihood, exp_pdf, sample_exp, x_min, x_max)

            y_intersection_1: float = bisezione_h(h, exp_pdf, sample_exp, x_min, t_0, par_max)
            y_intersection_2: float = bisezione_h(h, exp_pdf, sample_exp, t_0, x_max, par_max)

            sigma_ML: float = 0.5 * (y_intersection_2 - y_intersection_1)

            scarto: float = (par_max - t_0) / sigma_ML

            scarti.append(scarto)

        scarti_means.append(np.mean(scarti))
        scarti_devstd.append(np.std(scarti))

    # Plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 8 parte 2")
    ax.set_xlabel("N")
    ax.set_ylabel("y")

    x_coord = np.arange(N)
    ax.plot(x_coord, scarti_means, linestyle = "-", color = "red", label = "Media")
    ax.plot(x_coord, scarti_devstd, linestyle = "-", color = "blue", label = "Sigma")

    ax.legend(loc = "upper left")
    plt.savefig("es8_2.png")

    return

if __name__ == "__main__":
    main()