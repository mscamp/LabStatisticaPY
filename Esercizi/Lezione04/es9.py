"""
    ESERCIZIO 4.9 (da risolvere dopo aver seguito la lezione 5)
    Testa l'oggetto 'stats' dell'esercizio precedente con ciascuno dei metodi di generazione di numeri pseudo-casuali. In particolare:
    * Verifica che la varianza della distribuzione uniforme corrisponde al valore atteso, specificando la sua incertezza
    * Verifica che la varianza ottenuta usando il teorema centrale del limite corrisponda al valore atteso
"""

# Librerie
from scipy.stats import norm, uniform
from es8 import Stats
from random_methods import *
from matplotlib import pyplot as plt
import scienceplots

def main():
    
    # Plot
    plt.style.use(["grid"])
    fig, axes = plt.subplots(nrows = 2, ncols = 2)
    fig.suptitle("Esercizio 9", fontsize = 15)

    for i in range(2):
        for j in range(2):
            axes[i][j].set_xlabel("x")
            axes[i][j].set_ylabel("y")

    fig.tight_layout()

    # Sample size
    N = 10000

    # 1. Distribuzione uniforme
    x_min = -10.0
    x_max = 10.0
    sample_unif = Stats(gen_unif(x_min, x_max, N))

    # Confronto con varianza attesa
    unif_distribution = uniform(x_min, 20.0) # distribuzione uniforme su [-10.0, 10.0]
    unif_var = unif_distribution.stats(moments = "v") # valore vero della varianza
    sample_unif_var = sample_unif.var() # varianza campionaria

    print(f"Scarto delle varianze (distribuzione uniforme): {np.abs(unif_var - sample_unif_var)}")

    # Istogramma
    n_bins = sturges(N)
    bin_edges = np.linspace(x_min, x_max, n_bins)
    axes[0][0].hist(sample_unif.sample, bin_edges, color = "orange", label = "Uniforme", histtype = "step", density = True)
    axes[0][0].legend(loc = "lower right", fontsize = 8, fancybox = False, edgecolor = "black")

    # 2. Metodo TAC con distribuzione gaussiana
    media = 0.0
    sigma = 1.5
    gauss_distribution_TAC = norm(media, sigma)
    sample_TAC = Stats(gen_TAC(gauss_distribution_TAC.pdf, x_min, x_max, gauss_distribution_TAC.pdf(media), N))

    # Istogramma
    axes[0][1].hist(sample_TAC.sample, bin_edges, color = "red", label = "Gauss TAC", histtype = "step", density = True)
    axes[0][1].legend(loc = "upper right", fontsize = 8, fancybox = False, edgecolor = "black")

    # 3. Metodo della funzione inversa con distribuzione esponenziale
    x_min = 0.0
    x_max = 10.0
    mu = 1.5
    sample_inverse_exp_CDF = Stats(gen_inverse_exponential_CDF(mu, N))

    # Istogramma
    bin_edges = np.linspace(x_min, x_max, n_bins)
    axes[1][0].hist(sample_inverse_exp_CDF.sample, bin_edges, color = "blue", label = "Exp inverse CDF", histtype = "step", density = True)
    axes[1][0].legend(loc = "upper right", fontsize = 8, fancybox = False, edgecolor = "black")

    # 4. Teorema centrale del limite
    sample_TCL = Stats(gen_TCL_ms(media, sigma, N))

    # Confronto con varianza attesa
    x_min = -10.0
    x_max = 10.0
    sample_TCL_var = sample_TCL.var() # varianza campionaria

    print(f"Scarto delle varianze (distribuzione gaussiana con TCL): {np.abs(sigma - sample_TCL_var)}")

    # Istogramma
    bin_edges = np.linspace(x_min, x_max, n_bins)
    axes[1][1].hist(sample_TCL.sample, bin_edges, color = "lime", label = "Gauss TCL", histtype = "step", density = True)
    axes[1][1].legend(loc = "upper right", fontsize = 8, fancybox = False, edgecolor = "black")

    plt.savefig("es9.png")

    return

if __name__ == "__main__":
    main()
