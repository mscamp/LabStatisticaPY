"""
    ESERCIZIO 6.5
    Svolgi l'esercizio precedente impiegando una funzione ricorsiva
"""

# Librerie
from zeri_estremi import *
from matplotlib import pyplot as plt
import scienceplots

def g(x: float) -> float:
    return x**2 + 7.3 * x + 4.0

def main() -> None:

    # Variabili
    x_min: float = -10.0
    x_max: float = 10.0
    x_coord = np.linspace(x_min, x_max, 10000)

    # Determina il minimo
    g_min = find_min_recursive(g, x_min, x_max)
    print(f"Punto di minimo: {g_min}")
    print(f"Valore di g nel minimo: {g(g_min)}")

    # Plot
    plt.style.use(["science", "notebook", "grid"])
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 5")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    plt.plot(x_coord, g(x_coord), color = "red", label = "g(x)")
    plt.scatter(g_min, g(g_min), color = "blue", label = "Minimo")

    ax.legend()
    plt.show()

    return

if __name__ == "__main__":
    main()