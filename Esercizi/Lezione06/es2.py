"""
    ESERCIZIO 6.2
    Ripeti l'esercizio precedente utilizzando l'implementazione ricorsiva del metodo di bisezione
"""

# Librerie
from zeri_estremi import *
from matplotlib import pyplot as plt
import scienceplots

def g(x: float) -> float:
    return np.cos(x)

def main() -> None:

    # Variabili
    x_min: float = 0.0
    x_max: float = 4.0
    x_coord = np.linspace(x_min, x_max, 10000)

    # Determina lo zero di g
    zero: float = bisezione_ricorsiva(g, x_min, x_max)
    print(f"Zero di g in ({x_min}, {x_max}): {zero}")

    # Plot
    plt.style.use(["science", "notebook", "grid"])
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 2")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    plt.plot(x_coord, g(x_coord), color = "red", label = "g(x)")
    plt.scatter(zero, 0.0, color = "blue", label = "Zero")

    ax.legend()
    plt.show()

    return

if __name__ == "__main__":
    main()