"""
    ESERCIZIO 11.7
    Ripeti gli esercizi 1, 2, 3, 6 con un modello con andamento parabolico
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
    x_min: float = 0.0
    x_max: float = 10.0
    N_points: int = 10
    a_true: float = 0.3
    b_true: float = 0.0
    c_true: float = 0.0
    epsilon_sigma: float = 0.4
    x_coord: list[float] = gen_unif(x_min, x_max, N_points)
    y_coord: list[float] = []

    # Genera gl scarti
    epsilons: list[float] = gen_TCL_ms(0.0, epsilon_sigma, N_points)

    # Genera gli y_i
    for i in range(len(x_coord)):
        y_coord.append(phi(x_coord[i], a_true, b_true, c_true) + epsilons[i])

    # Errori su y (tutti uguali)
    y_sigma = epsilon_sigma * np.ones(N_points)

    # Fit con minimi quadrati
    least_squares = LeastSquares(x_coord, y_coord, y_sigma, phi)
    minuit_obj = Minuit(least_squares, a = -0.2, b = 4.5, c = -1.0)
    minuit_obj.migrad()
    minuit_obj.hesse()

    # Successo del fit
    print(f"Fit success: {minuit_obj.valid}")

    # Parametri stimati
    par_0 = minuit_obj.parameters[0]
    par_1 = minuit_obj.parameters[1]
    par_2 = minuit_obj.parameters[2]
    par_0_value = minuit_obj.values[0]
    par_1_value = minuit_obj.values[1]
    par_2_value = minuit_obj.values[2]
    par_0_sigma = minuit_obj.errors[0]
    par_1_sigma = minuit_obj.errors[1]
    par_2_sigma = minuit_obj.errors[2]

    print(f"Stima del parametro {par_0}: {par_0_value} +/ {par_0_sigma}")
    print(f"Stima del parametro {par_1}: {par_1_value} +/ {par_1_sigma}")
    print(f"Stima del parametro {par_2}: {par_2_value} +/ {par_2_sigma}")

    # Calcolo del Q^2
    qsquared: float = Q_squared(x_coord, y_coord, y_sigma, par_0_value, par_1_value, par_2_value)
    qsquared_minuit: float = minuit_obj.fval

    scarto: float = np.abs(qsquared - qsquared_minuit)

    print(f"Scarto tra i Q^2: {scarto}")

    # Gradi di libertà
    N_dof: int = minuit_obj.ndof
    print(f"Gradi di libertà: {N_dof}")

    # Matrice di covarianza
    print(minuit_obj.covariance)

    # Plot
    plt.style.use(["science", "notebook", "grid"])
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 7")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    phi_fit: list[float] = []

    for i in range(len(x_coord)):
        phi_fit.append(phi(x_coord[i], par_0_value, par_1_value, par_2_value))

    ax.errorbar(x_coord, y_coord, xerr = 0.0, yerr = y_sigma, color = "blue", linestyle = "", marker = "o", label = "Data")
    ax.plot(x_coord, phi_fit, color = "red", label = "Fit") 
    
    ax.legend(loc = "lower left")
    plt.savefig("es7.png")

    return

if __name__ == "__main__":
    main()