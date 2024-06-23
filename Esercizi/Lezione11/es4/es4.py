"""
    ESERCIZIO 11.4
    Usando la tecnica dei toy experiment, genera 10000 esperimenti di fit con il modello degli esercizi 
    precedenti e riempi un istogramma con i valori di Q^2. Calcola il chi^2 ridotto.
"""

# Librerie
import numpy as np
from matplotlib import pyplot as plt
import scienceplots
from model import *
from random_methods import *
from iminuit import Minuit
from iminuit.cost import LeastSquares

def main() -> None:
    
    # Variabili
    N_toys: int = 10000
    x_min: float = 0.0
    x_max: float = 10.0
    N_points: int = 10
    m_true: float = 0.5
    q_true: float = 1.1
    epsilon_sigma: float = 0.3
    qsquared_list: list[float] = []

    # Loop sui toy experiment
    for i in range(N_toys):
        x_coord: list[float] = gen_unif(x_min, x_max, N_points)
        y_coord: list[float] = []

        # Genera gl scarti
        epsilons: list[float] = gen_TCL_ms(0.0, epsilon_sigma, N_points)

        # Genera gli y_i
        for i in range(len(x_coord)):
            y_coord.append(phi(x_coord[i], m_true, q_true) + epsilons[i])

        # Errori su y (tutti uguali)
        y_sigma = epsilon_sigma * np.ones(N_points)

        # Fit con minimi quadrati
        least_squares = LeastSquares(x_coord, y_coord, y_sigma, phi)
        minuit_obj = Minuit(least_squares, m = 0.0, q = 1.0)
        minuit_obj.migrad()
        minuit_obj.hesse()

        qsquared_list.append(minuit_obj.fval)

    # Chi quadro ridotto
    N_dof: int = minuit_obj.ndof
    chi2_rid: float = np.mean(qsquared_list) / N_dof
    print(f"Chi^2 ridotto: {chi2_rid}")

    # Plot
    plt.style.use(["science", "notebook", "grid"])
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 4")
    ax.set_xlabel("Q^2")
    ax.set_ylabel("Numero di eventi per bin")

    # Istogramma
    x_min_hist: float = 0.0
    x_max_hist: float = 30.0
    n_bins: int = sturges(len(qsquared_list))
    bin_edges = np.linspace(x_min_hist, x_max_hist, n_bins)

    ax.hist(qsquared_list, bin_edges, color = "orange", label = "Distribuzione di Q^2", density = True)
    
    ax.legend()
    plt.savefig("es4.png")

    return

if __name__ == "__main__":
    main()
