"""
    ESERCIZIO 1.4
    Scrivi un programma che, usando un ciclo for, scrive la successione di Fibonacci fino al termine
    n-esimo e la mette in un dict, dove la key è l'indice di ciascun termine e la value è il valore
    numerico del termine.
"""

# Librerie
import sys

def fibonacci_sequence(n):
    """ 
        Prende in input un numero intero n e restituisce un dictionary contenente i primi n termini della
        successione di Fibonacci.
    """

    # Variabili
    fibonacci_n = {}

    # Crea la successione
    for i in range(0, n):
        if i == 0:
            fibonacci_n[i] = 1

        elif i == 1:
            fibonacci_n[i] = 1

        else: 
            fibonacci_n[i] = (fibonacci_n[i-2] + fibonacci_n[i-1])

    return fibonacci_n

def main():

    # Controllo argomenti passati da riga di comando
    if len(sys.argv) != 2:
        exit(1)

    # Variabili
    n = int(sys.argv[1])
    fibonacci_dict = fibonacci_sequence(n) 
    phi = (fibonacci_dict[n-1] / fibonacci_dict[n-2])

    # Stampa a schermo
    print(fibonacci_dict)
    print(f"I primi {n} termini della successione sono: {fibonacci_dict.values()}")
    print(f"Valore approssimato di phi: {phi}")

    return

if __name__ == "__main__":
    main()