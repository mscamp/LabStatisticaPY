"""
    ESERCIZIO 8.6
    Implementa il calcolo dell'integrale dell'esercizio precedente in un loop sul numero dei punti generati N, in cui viene mostrato il
    valore dell'integrale e il suo errore al variare di N. Usa uno scatter plot per visualizzare il valore dell'integrale e la sua
    incertezza in funzione di N in scala logaritmica.
"""

# Librerie
import numpy as np
from MC_integration import hit_or_miss
from matplotlib import pyplot as plt
import scienceplots

def f(x: float) -> float:
    return np.sin(x)

# Variabili
def main() -> None:
    N_max: int = 100000
    x_min: float = 0.0
    x_max: float = np.pi
    y_max: float = 1.0
    integral_values: list[float] = []
    integral_errors: list[float] = []
    x_coord = np.arange(1, N_max, 1000)

    # Calcola l'integrale al variare di N
    for N in range(1, N_max, 1000):
        res: list[float] = hit_or_miss(f, x_min, x_max, y_max, N)
        integral_values.append(res[0])
        integral_errors.append(res[1])

        print(f"Integrale di sin(x) tra {x_min} e {x_max}: {res[0]} +/- {res[1]} per N = {N}")

    # Scatter plot
    plt.style.use(["science", "notebook", "grid"])
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 6")
    ax.set_xlabel("log(N)")
    ax.set_ylabel("y")
    ax.set_xscale("log")

    ax.plot(x_coord, integral_values, "-", color = "red", label = "Value") 
    ax.plot(x_coord, integral_errors, "-", color = "blue", label = "Error") 

    plt.show()

    return

if __name__ == "__main__":
    main()