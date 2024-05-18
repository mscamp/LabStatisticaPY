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