"""
    ESERCIZIO 6.1
    Determina lo zero della funzione g(x) = cos(x) usando il metodo di bisezione nell'intervallo (0, 4). Quali controlli sono stati 
    omessi nell'esempio presentato a lezione che potrebbero velocizzare l'esecuzione della funzione?
"""

# Librerie
from zeri_estremi import *
from matplotlib import pyplot as plt
import scienceplots

def g(x: float):
    return np.cos(x)

def main() -> None:

    # Variabili
    x_min: float = 0.0
    x_max: float = 4.0
    x_coord = np.linspace(x_min, x_max, 10000)

    # Determina lo zero di g
    zero: float = bisezione(g, x_min, x_max)
    print(f"Zero di g in ({x_min}, {x_max}): {zero}")

    # Plot
    plt.style.use(["science", "notebook", "grid"])
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title("Esercizio 1")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    plt.plot(x_coord, g(x_coord), color = "red", label = "g(x)")
    plt.scatter(zero, 0.0, color = "blue", label = "Zero")

    ax.legend()
    plt.show()

    return

if __name__ == "__main__":
    main()