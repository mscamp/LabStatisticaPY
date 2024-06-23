"""
    ESERCIZIO 10.1
    Scrivi una libreria per determinare il valore del parametro t_0 di una distribuzione esponenziale a partire da un campione di numeri pseudo-casuali distribuiti
    esponenzialmente. Confronta il risultato ottenuto con la media del campione.

    ESERCIZIO 10.2
    Plotta la loglikelihood mettendo in evidenza il suo massimo

    ESERCIZIO 10.3
    Modifica la funzione find_max_likelihood, aggiungendo la stampa degli estremi dell'intervallo di ricerca del massimo per ciascuna iterazione, per osservare la
    restrizione dell'intervallo durante l'esecuzione del programma
"""

# Librerie
from random_methods import *
from max_likelihood import *
from matplotlib import pyplot as plt
import scienceplots

def exp_pdf(x: float, t_0: float) -> float:
    return (1.0 / t_0) * np.exp((-1.0) * (x / t_0))

def find_max_likelihood_es3(g, pdf, sample: list[float], x_min: float, x_max: float, precision: float = 0.0001) -> float: 

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

        print(f"Intervallo: [{x_min}, {x_max}]")

    return 0.5 * (x_min + x_max)

def main() -> None:

    # Variabili
    t_0: float = 1.5
    N: int = 10000
    sample_exp: list[float] = gen_inverse_exponential_CDF(t_0, N)
    sample_mean: float = np.mean(sample_exp)

    # Stima di t_0 con ML
    x_min: float = 0.5
    x_max: float = 2.0
    par_max: float = find_max_likelihood_es3(loglikelihood, exp_pdf, sample_exp, x_min, x_max)

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

    # Plot
    plt.style.use(["science", "notebook", "grid"])
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 2")
    ax.set_xlabel("t_0")
    ax.set_ylabel("loglikelihood(t_0)")

    ax.plot(x_coord, ll, color = "red", label = "l(t_0; x)")
    ax.scatter(par_max, loglikelihood(exp_pdf, sample_exp, par_max), color = "blue", label = "Massimo")

    ax.legend(fancybox = False, edgecolor = "black")
    plt.show()

    return

if __name__ == "__main__":
    main()