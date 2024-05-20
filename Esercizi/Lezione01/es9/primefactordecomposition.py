# Librerie
import operator
import functools

# Funzioni
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

def prime_decomposition(n):
    """ Determina la scomposizione in fattori primi di un numero intero positivo, ritorna una lista """

    # Controlla che n sia positivo
    if n <= 0: 
        print("Inserire un numero strettamente positivo.")
        return None

    # Variabili
    prime_factors_of_n = []

    # Caso banale: n è primo
    if is_prime(n):
        prime_factors_of_n.append(n)
        return prime_factors_of_n
    
    # Caso non banale
    primes_up_to_n = find_primes(n)

    while is_prime(n) == False:
        for prime in primes_up_to_n:
            if (n % prime == 0):
                prime_factors_of_n.append(prime)
                n = int(n / prime)
                break

    prime_factors_of_n.append(n)

    return prime_factors_of_n

def test_function():
    for n in range(2, 100):
        prime_factors = prime_decomposition(n)
        res = functools.reduce(operator.mul, prime_factors, 1) # Moltiplica tra loro gli elementi della lista

        if res == n:
            print(f"{n}: OK")
        
        else:
            print(f"{n}: ERROR")