""" 
    ESERCIZIO 1.5
    Scrivi una funzione che restituisce la successione di Fibonacci fino al termine n-esimo in una lista e 
    a) Crea una nuova lista che contenga solo gli elementi con indice pari di tale lista
    b) Crea una nuova lista che contenga solo gli elementi con indice dispari di tale lista
    c) Inserisci la funzione in una libreria e importala nel programma
"""

# Librerie
import sys
from fibonacci import fibonacci_sequence

def main():

    # Controllo argomenti passati da riga di comando
    if len(sys.argv) != 2:
        exit(1)

    # Variabili
    n = int(sys.argv[1])
    fibonacci_list = fibonacci_sequence(n)
    fibonacci_list_even = [fibonacci_list[i] for i in range(0, len(fibonacci_list), 2)]
    fibonacci_list_odd = [fibonacci_list[i] for i in range(1, len(fibonacci_list), 2)]

    # Stampa a schermo
    print(f"Fibonacci: {fibonacci_list}")
    print(f"Fibonacci pari: {fibonacci_list_even}")
    print(f"Fibonacci dispari: {fibonacci_list_odd}")

    return

if __name__ == "__main__":
    main()