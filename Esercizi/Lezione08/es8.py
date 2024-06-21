"""
    ESERCIZIO 8.8
    Implementa il calcolo dell'integrale dell'esercizio precedente in un loop sul numero dei punti generati N, in cui viene mostrato il
    valore dell'integrale e il suo errore al variare di N. Usa uno scatter plot per visualizzare il valore dell'integrale e la sua
    incertezza in funzione di N in scala logaritmica. Infine, fai un confronto grafico con i valori ottenuti nell'esercizio 6.
"""

# Librerie
import numpy as np
from MC_integration import *
from matplotlib import pyplot as plt
import scienceplots

def f(x: float) -> float:
    return np.sin(x)

def main() -> None:
    
    # Variabili
    N_max: int = 100000
    x_min: float = 0.0
    x_max: float = np.pi
    y_max: float = 1.0
    integral_values_hitormiss: list[float] = []
    integral_errors_hitormiss: list[float] = []
    integral_values_crudeMC: list[float] = []
    integral_errors_crudeMC: list[float] = []
    x_coord = np.arange(1, N_max, 1000)

    # Calcola l'integrale al variare di N
    for N in range(1, N_max, 1000):
        res_hitormiss: list[float] = hit_or_miss(f, x_min, x_max, y_max, N)
        res_crudeMC: list[float] = crude_MC(f, x_min, x_max, N)

        integral_values_hitormiss.append(res_hitormiss[0])
        integral_errors_hitormiss.append(res_hitormiss[1])

        integral_values_crudeMC.append(res_crudeMC[0])
        integral_errors_crudeMC.append(res_crudeMC[1])

        print(f"----- N = {N} -----")
        print(f"Integrale di sin(x) tra {x_min} e {x_max}: {res_hitormiss[0]} +/- {res_hitormiss[1]} (hit or miss)")
        print(f"Integrale di sin(x) tra {x_min} e {x_max}: {res_crudeMC[0]} +/- {res_crudeMC[1]} (crude MC)")
        print(f"------------------")
        print('\n')

    # Scatter plot
    plt.style.use(["science", "notebook", "grid"])
    fig, axes = plt.subplots(nrows = 1, ncols = 2)
    fig.suptitle("Esercizio 6", y = 0.87, fontsize = 20)
    fig.text(0.5, 0.05, "log(N)", ha = "center", size = 15)
    fig.tight_layout(pad = 3)
    axes[0].set_ylabel("Values")
    axes[1].set_ylabel("Errors")
    axes[0].set_xscale("log")
    axes[1].set_xscale("log")

    axes[0].plot(x_coord, integral_values_hitormiss, "-", color = "red", label = "Value (hit or miss)") 
    axes[1].plot(x_coord, integral_errors_hitormiss, "-", color = "red", label = "Error (hit or miss)") 
    axes[0].plot(x_coord, integral_values_crudeMC, "-", color = "blue", label = "Value (crude MC)") 
    axes[1].plot(x_coord, integral_errors_crudeMC, "-", color = "blue", label = "Error (crude MC)") 

    axes[0].legend(loc = "lower right", fontsize = 10)
    axes[1].legend(loc = "lower right", fontsize = 10)

    plt.show()

    return

if __name__ == "__main__":
    main()