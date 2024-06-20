"""
    ESERCIZIO 6.6
    Svolgere nuovamente i due esercizi precedenti trovando il massimo di una funzione a scelta
"""

# Librerie
from zeri_estremi import *
from matplotlib import pyplot as plt
import scienceplots

def g(x: float) -> float:
    return (-1.0) * x**2 + 6.5 * x - 7.0

def main() -> None:

    # Variabili
    x_min: float = 0.0
    x_max: float = 5.0
    x_coord = np.linspace(x_min, x_max, 10000)

    # Determina il massimo
    g_max = find_max(g, x_min, x_max)
    print("--- SEZIONE AUREA ---")
    print(f"Punto di massimo: {g_max}")
    print(f"Valore di g nel massimo: {g(g_max)}")
    print('\n')

    # Determina il massimo (ricorsivo)
    g_max_rec = find_max_recursive(g, x_min, x_max)
    print("--- SEZIONE AUREA RICORSIVA ---")
    print(f"Punto di massimo: {g_max_rec}")
    print(f"Valore di g nel massimo: {g(g_max_rec)}")

    # Plot
    plt.style.use(["science", "notebook", "grid"])
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 6")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    plt.plot(x_coord, g(x_coord), color = "red", label = "g(x)")
    plt.scatter(g_max, g(g_max), color = "blue", label = "Massimo")
    plt.scatter(g_max_rec, g(g_max_rec), color = "lime", label = "Massimo (ricorsivo)")

    ax.legend()
    plt.show()

    return

if __name__ == "__main__":
    main()