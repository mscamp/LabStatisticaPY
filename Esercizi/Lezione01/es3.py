"""
    ESERCIZIO 1.3
    Scrivi un programma che, usando un ciclo while, scrive la successione di Fibonacci fino al termine
    n-esimo e la mette in una lista. Calcola il valore approssimato di phi.
"""

# Librerie
import sys

def fibonacci_sequence(n):
    """ 
        Prende in input un numero intero n e restituisce una lista contenente i primi n termini della
        successione di Fibonacci.
    """

    # Variabili
    fibonacci_n = []
    i = 0

    # Crea la successione
    while i < n:
        if i == 0:
            fibonacci_n.append(1)

        elif i == 1:
            fibonacci_n.append(1)

        else: 
            fibonacci_n.append(fibonacci_n[i-2] + fibonacci_n[i-1])

        i += 1

    return fibonacci_n

def main():
    # Controllo argomenti passati da riga di comando
    if len(sys.argv) != 2:
        exit(1)

    # Variabili
    n = int(sys.argv[1])
    fibonacci_list = fibonacci_sequence(n) 
    phi = (fibonacci_list[n-1] / fibonacci_list[n-2])

    # Stampa a schermo
    print(f"I primi {n} termini della successione sono: {fibonacci_list}")
    print(f"Valore approssimato di phi: {phi}")

    return

if __name__ == "__main__":
    main()