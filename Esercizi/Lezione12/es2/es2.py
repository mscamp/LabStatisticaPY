"""
    ESERCIZIO 12.2
    Genera un file "dati_2.txt" contenente 10000 eventi distribuiti secondo una gaussiana. Scrivi un programma che fitta gli eventi salvati nel file dati_2.txt 
    usando la binned maximum likelihood e la unbinned maximum likelihood, dopodiché confronta i risultati ottenuti dai due metodi
"""

# Librerie
import numpy as np
from random_methods import *
from iminuit import Minuit
from iminuit.cost import ExtendedBinnedNLL
from iminuit.cost import UnbinnedNLL
from matplotlib import pyplot as plt
from scipy.stats import norm
from scipy.integrate import quad

def mod_total_binned(bin_edges, N_signal: int, mu: float, sigma: float) -> float:
    return N_signal * norm.cdf(bin_edges, mu, sigma)

def mod_total_binned_plot(x: float, N_signal: int, mu: float, sigma: float) -> float:
    return N_signal * norm.pdf(x, mu, sigma)

def mod_total_binned_plot_normalized(x: float, N_signal: int, mu: float, sigma: float) -> float:
    return mod_total_binned_plot(x, N_signal, mu, sigma) / quad(mod_total_binned_plot, -np.inf, np.inf, args=(N_signal, mu, sigma))[0]

def mod_total_unbinned(x: float, mu: float, sigma: float) -> float:
    return norm.pdf(x, mu, sigma)

def genera_eventi(N: int, media: float, sigma: float) -> str:

    # Variabili
    sample: list[float] = gen_TCL_ms(media, sigma, N)
    file_name: str = "/home/scampo/Documents/Università/II anno/I semestre/Laboratorio di statistica/Python/Esercizi/Lezione12/es2/dati_2.txt"

    with open(file_name, "w") as output_file:
        for element in sample:
            output_file.write(f"{element:.4f}" + '\n')

    return file_name

def main() -> None:

    # Variabili
    media_true = 0.0
    sigma_true = 1.0
    N_events: int = 10000
    file_name: str = genera_eventi(N_events, media_true, sigma_true)

    # Importa gli eventi
    sample = np.loadtxt(file_name)
    x_min: float = np.floor(np.mean(sample) - 3.0 * np.std(sample))
    x_max: float = np.ceil(np.mean(sample) + 3.0 * np.std(sample))
    n_bins: int = sturges(len(sample))
    x_coord = np.linspace(x_min, x_max, N_events)

    # Fit con binned ML
    bin_content, bin_edges = np.histogram(sample, n_bins, range = (x_min, x_max))
    cost_func = ExtendedBinnedNLL(bin_content, bin_edges, mod_total_binned)
    minuit_obj = Minuit(cost_func, N_signal = N_events, mu = np.mean(sample), sigma = np.std(sample))
    minuit_obj.migrad()

    print(f"Fit success (binned): {minuit_obj.valid}")
    print(minuit_obj.params)

    # Plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 2 - Binned ML")
    ax.set_xlabel("Eventi")
    ax.set_ylabel("Numero di eventi per bin")

    ax.hist(sample, bin_edges, color = "orange", label = "Data", density = True)
    ax.plot(x_coord, mod_total_binned_plot_normalized(x_coord, minuit_obj.values["N_signal"], minuit_obj.values["mu"], minuit_obj.values["sigma"]), color = "red", label = "Model")

    ax.legend()
    plt.savefig("es2_binned.png")

    # Fit con unbinned ML
    cost_func_unb = UnbinnedNLL(sample, mod_total_unbinned)
    minuit_obj_unb = Minuit(cost_func_unb, mu = np.mean(sample), sigma = np.std(sample))
    minuit_obj_unb.migrad()

    print(f"Fit success (unbinned): {minuit_obj_unb.valid}")
    print(minuit_obj_unb.params)

    # Plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 2 - Unbinned ML")
    ax.set_xlabel("Eventi")
    ax.set_ylabel("Numero di eventi per bin")

    ax.hist(sample, bin_edges, color = "orange", label = "Data", density = True)
    ax.plot(x_coord, mod_total_unbinned(x_coord, minuit_obj_unb.values["mu"], minuit_obj_unb.values["sigma"]), color = "red", label = "Model")

    ax.legend()
    plt.savefig("es2_unbinned.png")

    return

if __name__ == "__main__":
    main()