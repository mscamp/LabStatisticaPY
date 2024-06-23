"""
    ESERCIZIO 10.7
    Utilizza la tecnica dei toy experiment per plottare la distribuzione dello stimatore di t_0:
    * Sovrapponi l'istogramma al plot di par_max e dell'intervallo di confidenza dell'esercizio precedente
    * Confronta il valore di sigma dell'esercizio precedente con quello calcolato a partire dalla distribuzione dello stimatore
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
    N: int = 500
    N_toys: int = 1000
    par_max_list: list[float] = []
    x_min: float = 0.5
    x_max: float = 2.0
    
    # Loop sui toys
    for i in range(N_toys):
        sample_exp: list[float] = gen_inverse_exponential_CDF(t_0, N)
        par_max: float = find_max_likelihood(loglikelihood, exp_pdf, sample_exp, x_min, x_max)
        par_max_list.append(par_max)

    # Stima dell'incertezza con metodo grafico
    sample_exp: list[float] = gen_inverse_exponential_CDF(t_0, N)
    par_max: float = find_max_likelihood(loglikelihood, exp_pdf, sample_exp, x_min, x_max)

    y_intersection_1: float = bisezione_h(h, exp_pdf, sample_exp, x_min, t_0, par_max)
    y_intersection_2: float = bisezione_h(h, exp_pdf, sample_exp, t_0, x_max, par_max)

    sigma_ML: float = 0.5 * (y_intersection_2 - y_intersection_1)

    # Stima dell'incertezza dal campione
    sigma_sample: float = np.std(par_max_list)

    # Confronto delle sigma
    print(f"Scarto tra le sigma: {np.abs(sigma_ML - sigma_sample)}")

    # Plot
    plt.style.use(["science", "notebook"])
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 7")
    ax.set_xlabel("t_0")
    ax.set_ylabel("Eventi per bin")

    # Istogramma
    n_bins: int = sturges(len(par_max_list))
    bin_edges = np.linspace(x_min, x_max, n_bins)

    ax.hist(par_max_list, bin_edges, color = "orange", label = "Distribuzione di t_0 hat", density = True)

    # Plot delle rette
    vertical_limits = ax.get_ylim()

    ax.plot([y_intersection_1, y_intersection_1], vertical_limits, "--", color = "green", label = "t_0 - sigma")
    ax.plot([y_intersection_2, y_intersection_2], vertical_limits, "--", color = "green", label = "t_0 + sigma")
    ax.plot([par_max, par_max], vertical_limits, "--", color = "blue", label = "t_0 stimato")

    ax.legend(loc = "upper left", fontsize = 10)
    plt.show()

    return

if __name__ == "__main__":
    main()