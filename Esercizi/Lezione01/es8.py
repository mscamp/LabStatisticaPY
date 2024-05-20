""" 
    ESERCIZIO 1.8
    Scrivi un programma che trovi la lista dei numeri primi minori di 100, sapendo che 2 è primo
"""

def is_prime(n, i = 2):
    """ Determina se un numero è primo con un algoritmo ricorsivo. Restituisce un valore boolean. """

    # Caso base
    if n < 2: 
        return False

    elif n == 2:
        return True

    # Determina se n è primo
    elif n % i == 0:
        return False

    elif i**2 > n:
        return True

    # Passo ricorsivo
    return is_prime(n, i + 1)


def find_primes(N):
    """ Determina i numeri primi fino a N e li restituisce sottoforma di una lista """

    # Variabili
    primes = []

    for n in range(N+1):
        if is_prime(n):
            primes.append(n)

    return primes

def main():

    # Variabili
    N = 100
    primes_under_100 = find_primes(N)

    # Stampa a schermo
    print(primes_under_100)

    return

if __name__ == "__main__":
    main()