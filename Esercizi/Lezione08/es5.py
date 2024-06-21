"""
    ESERCIZIO 8.5
    Implementa il metodo di integrazione hit-or-miss con la funzione f(x) = sin(x):
    * Scrivi l'algoritmo che calcola l'integrale come funzione esterna al main, in modo che prenda in input gli estremi dell'intervallo
    di integrazione e gli estremi sull'asse y, oltre al numero di coppie da generare
    * Fai in modo che l'algoritmo restituisca un contenitore con due elementi, cioé il valore dell'integrale e l'incertezza associata
"""

# Librerie
import numpy as np
from MC_integration import hit_or_miss

def f(x: float) -> float:
    return np.sin(x)

def main() -> None:
    
    # Variabili
    N: int = 10000
    x_min: float = 0.0
    x_max: float = np.pi
    y_max: float = 1.0

    # Calcola l'integrale
    res: list[float] = hit_or_miss(f, x_min, x_max, y_max, N)

    # Stampa a schermo il risultato
    print(f"Integrale di sin(x) tra {x_min} e {x_max}: {res[0]} +/- {res[1]}")

    return

if __name__ == "__main__":
    main()