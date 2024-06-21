"""
    ESERCIZIO 8.9
    Usa il metodo di integrazione hit-or-miss per stimare l'integrale di una distribuzione di probabilità gaussiana con media = 0, sigma = 1 in un generico intevallo
    [a, b]. Calcola poi l'integrale della gaussiana nell'intervallo [-k * sigma, k * sigma] con k che varia da 1 a 5
"""

# Librerie
from MC_integration import hit_or_miss
from scipy.stats import norm

def main() -> None:

    # Variabili
    N: int = 100000
    media: float = 0.0
    sigma: float = 1.0
    gauss = norm(media, sigma)

    # Integrale
    for k in range(1, 6):
        res: list[float] = hit_or_miss(gauss.pdf, -k * sigma, k * sigma, gauss.pdf(media), N)
        print(f"Integrale tra -{k} * sigma e {k} * sigma: {res[0]} +/- {res[1]}")

    return

if __name__ == "__main__":
    main()