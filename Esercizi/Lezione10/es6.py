"""
    ESERCIZIO 10.6
    Usa il metodo di bisezione per trovare i punti par_max - sigma e par_max + sigma dell'esercizio 1. Plotta il profilo della 
    loglikelihood, il valore dello stimatore e l'intervallo di confidenza, insieme alla retta orizzontale utilizzata per determinarlo
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
    N: int = 10000
    sample_exp: list[float] = gen_inverse_exponential_CDF(t_0, N)
    sample_mean: float = np.mean(sample_exp)

    # Stima di t_0 con ML
    x_min: float = 0.5
    x_max: float = 2.0
    par_max: float = find_max_likelihood(loglikelihood, exp_pdf, sample_exp, x_min, x_max)

    # Stima dell'incertezza
    y_intersection_1 = bisezione_h(h, exp_pdf, sample_exp, x_min, t_0, par_max)
    y_intersection_2 = bisezione_h(h, exp_pdf, sample_exp, t_0, x_max, par_max)

    sigma_ML = 0.5 * (y_intersection_2 - y_intersection_1)

    print(f"Valore di t_0 che massimizza la likelihood: {par_max}")
    print(f"Incertezza associata: {sigma_ML}")
    print(f"Scarto con la media campionaria: {np.abs(par_max - sample_mean)}")

    # Valori della loglikelihood in funzione di t_0
    x_coord = np.linspace(x_min, x_max, 1000)
    ll = np.arange(0.0, len(x_coord))

    for i in range(len(x_coord)):
        ll[i] = loglikelihood(exp_pdf, sample_exp, x_coord[i])

    # Plot likelihood
    plt.style.use(["science", "notebook", "grid"])
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 6")
    ax.set_xlabel("t_0")
    ax.set_ylabel("loglikelihood(t_0)")

    ax.plot(x_coord, ll, color = "red", label = "l(t_0; x)")

    # Plot delle rette
    vertical_limits = ax.get_ylim()

    ax.plot([y_intersection_1, y_intersection_1], vertical_limits, "--", color = "blue")
    ax.plot([y_intersection_2, y_intersection_2], vertical_limits, "--", color = "blue")
    ax.plot([par_max, par_max], vertical_limits, "--", color = "orange")
    ax.axhline(y = loglikelihood(exp_pdf, sample_exp, par_max), color = "orange", linestyle = "--")
    ax.scatter(par_max, loglikelihood(exp_pdf, sample_exp, par_max), color = "pink", label = "Massimo")

    ax.legend(fancybox = False, edgecolor = "black")
    plt.show()

    return

if __name__ == "__main__":
    main()