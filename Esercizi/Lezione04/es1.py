"""
    ESERCIZIO 4.1
    Scrivi una funzione che implementi un generatore lineare congruenziale di numeri pseudo-casuali, usando i parametri
    * M = 2147483647
    * A = 214013
    * C = 2531011
"""

def generatore_lineare_congruenziale(x: int, M: int, A: int, C: int) -> int:
    return (A * x + C) % M

def main() -> None:

    # Parametri
    M: int = 2147483647
    A: int = 214013
    C: int = 2531011

    # Variabili
    x_0: int = 14 # seed
    sequence: list[int] = [x_0]

    # Genera la sequenza di numeri pseudo-casuali
    print(f"Seed: {x_0}")

    for i in range(10):
        sequence.append(generatore_lineare_congruenziale(sequence[i], M, A, C))
        print(f"Elemento {i + 1}: {sequence[-1]}")

    return

if __name__ == "__main__":
    main()