"""
    ESERCIZIO 12.1
    Scrivi un programma che esegua un fit dei dati salvati nel file "dati.txt":
    * Determina l'intervallo e il binning dell'istogramma usato per il fit dal campione, scrivendo algoritmi
    appropriati per determinare il minimo e il massimo del campione e una stima ragionevole del numero di bin
    da utilizzare
    * Determina i valori iniziali dei parametri del fit usando le tecniche descritte a lezione
    * Stampa a schermo i risultati del fit 
    * Plotta l'istogramma e il modello sovrapposti
    * Stampa la matrice di covarianza
"""

# Librerie
import numpy as np
from random_methods import sturges
from scipy.stats import norm, expon
from iminuit import Minuit
from iminuit.cost import ExtendedBinnedNLL
from matplotlib import pyplot as plt
from scipy.integrate import quad

# Modello usato per il fit
def mod_total(bin_edges, N_signal: int, mu: float, sigma: float, N_background: int, t_0: float):
    return N_signal * norm.cdf(bin_edges, mu, sigma) + N_background * expon.cdf(bin_edges, 0.0, t_0)

def mod_total_plot(x: float, N_signal: int, mu: float, sigma: float, N_background: int, t_0: float):
    return N_signal * norm.pdf(x, mu, sigma) + N_background * expon.pdf(x, 0.0, t_0)

def mod_total_plot_normalized(x: float, N_signal: int, mu: float, sigma: float, N_background: int, t_0: float):
    return mod_total_plot(x, N_signal, mu, sigma, N_background, t_0) / quad(mod_total_plot, 0.0, np.inf, args=(N_signal, mu, sigma, N_background, t_0))[0]

def main() -> None:

    # Lettura del file di testo
    file_name: str = "/home/scampo/Documents/Università/II anno/I semestre/Laboratorio di statistica/Python/Esercizi/Lezione12/es1/dati.txt"
    sample = np.loadtxt(file_name)

    # Valori per istogramma
    x_min: float = np.floor(np.min(sample))
    x_max: float = np.ceil(np.max(sample))
    n_bins: int = sturges(len(sample))
    x_range: tuple = (x_min, x_max)
    bin_content, bin_edges = np.histogram(sample, bins = n_bins, range = x_range)
    n_events: int = np.sum(bin_content)
    x_coord = np.linspace(x_min, x_max, 10000)

    # Valori iniziali per il fit
    mu_zero: float = np.mean(sample) 
    sigma_zero: float = np.std(sample) 
    N_signal_zero: int = n_events
    N_background_zero: int = n_events
    t_0_zero: float = 1.0

    # Cost function e minuit object
    cost_func = ExtendedBinnedNLL(bin_content, bin_edges, mod_total)
    minuit_obj = Minuit(cost_func, N_signal = N_signal_zero, mu = mu_zero, sigma = sigma_zero, N_background = N_background_zero, t_0 = t_0_zero)

    # Costringe i seguenti parametri ad essere positivi
    minuit_obj.limits["N_signal", "N_background", "sigma", "t_0"] = (0, None)

    # Fit sul rumore
    minuit_obj.values["N_signal"] = 0
    minuit_obj.fixed["N_signal", "mu", "sigma"] = True

    bin_centres = 0.5 * (bin_edges[1:] + bin_edges[:-1])
    cost_func.mask = (bin_centres < 5) | (15 < bin_centres)
    
    minuit_obj.migrad()
    minuit_obj.minos()
    print(minuit_obj.valid)

    # Fit sul segnale
    cost_func.mask = None
    minuit_obj.fixed = False
    minuit_obj.fixed["N_background", "t_0"] = True
    minuit_obj.values["N_signal"] = n_events - minuit_obj.values["N_background"]

    minuit_obj.migrad()
    minuit_obj.minos()
    print(minuit_obj.valid)

    # Fit finale
    minuit_obj.fixed = False
    minuit_obj.migrad()
    minuit_obj.minos()

    # Analisi dei risultati del fit
    print(f"Successo del fit: {minuit_obj.valid}")

    print(f"N_signal: {minuit_obj.values["N_signal"]} +/- {minuit_obj.errors["N_signal"]}")
    print(f"Mu: {minuit_obj.values["mu"]} +/- {minuit_obj.errors["mu"]}")
    print(f"Sigma: {minuit_obj.values["sigma"]} +/- {minuit_obj.errors["sigma"]}")
    print(f"N_background: {minuit_obj.values["N_background"]} +/- {minuit_obj.errors["N_background"]}")
    print(f"t_0: {minuit_obj.values["t_0"]} +/- {minuit_obj.errors["t_0"]}")

    print(minuit_obj.params)
    print(minuit_obj.covariance)
    print(minuit_obj.covariance.correlation)

    # Plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 1")
    ax.set_xlabel("Eventi")
    ax.set_ylabel("Numero di eventi per bin")

    ax.hist(sample, bin_edges, color = "orange", label = "Data", density = True)
    ax.plot(x_coord, mod_total_plot_normalized(x_coord, minuit_obj.values["N_signal"], minuit_obj.values["mu"], minuit_obj.values["sigma"], minuit_obj.values["N_background"], minuit_obj.values["t_0"]), color = "red", label = "Model")

    ax.legend()
    plt.savefig("es1.png")

    return

if __name__ == "__main__":
    main()
