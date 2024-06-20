"""
    ESERCIZIO 6.3
    Implementa una funzione che calcoli il fattoriale di un numero intero usando una funzione ricorsiva
"""

def fact(n: int) -> int:

    # Controllo argomento
    if type(n) != int:
        raise TypeError("Il numero n deve essere intero")

    # Caso base
    if n == 0:
        return 1
    
    # Ricorsione
    return n * fact(n - 1)

def main() -> None:

    # Variabili
    n = 6
    
    # Calcola il fattoriale
    n_fattoriale = fact(n)
    print(f"Fattoriale di {n}: {n_fattoriale}")

    return

if __name__ == "__main__":
    main()