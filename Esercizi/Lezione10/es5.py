"""
    ESERCIZIO 10.5
    Mostra graficamente che, all'aumentare del numero di eventi del campione, il profilo della loglikelihood diventa più stretto.
"""

# Librerie
from random_methods import *
from max_likelihood import *
from matplotlib import pyplot as plt

def exp_pdf(x: float, t_0: float) -> float:
    return (1.0 / t_0) * np.exp((-1.0) * (x / t_0))

def main() -> None:

    # Plot
    fig, axes = plt.subplots(nrows = 3, ncols = 3)

    fig.suptitle("Esercizio 5")
    fig.tight_layout()

    # Variabili
    t_0: float = 1.5
    N: int = 9000
    N_step: int = 1000
    list_of_ll: list[list[float]] = []
    count: int = 0
    x_min: float = 0.5
    x_max: float = 2.0
    x_coord = np.linspace(x_min, x_max, N_step)

    for i in range(1, N, N_step):
        sample_exp: list[float] = gen_inverse_exponential_CDF(t_0, N)

        # Stima di t_0 con ML
        par_max: float = find_max_likelihood(loglikelihood, exp_pdf, sample_exp, x_min, x_max)

        # Valori della loglikelihood in funzione di t_0
        ll = np.arange(0.0, len(x_coord))

        for j in range(len(x_coord)):
            ll[j] = loglikelihood(exp_pdf, sample_exp, x_coord[j])

        list_of_ll.append(ll)

    for i in range(3):
        for j in range(3):
            axes[i][j].set_title(f"N = {(count + 1) * N_step}")
            axes[i][j].plot(x_coord, list_of_ll[count], color = "red", label = "l(t_0; x)")
            count += 1

    plt.show()

    return

if __name__ == "__main__":
    main()