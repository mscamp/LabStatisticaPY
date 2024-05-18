"""
    ESERCIZIO 1.1
    Scrivi un programma che prende in input un numero intero e determina se esso sia divisibile per 2,3,5,7.
    Incapsula il check in una funzione che prende in input due numeri e scrivi un programma che chieda di
    inserire due numeri e controlla se il primo numero sia divisibile per il secondo
"""

def check_if_divisible(x, y):
    """ Controlla se il numero intero x è divisibile per y.
        Restituisce un valore boolean True se questo si verifica, False altrimenti. """

    if (x % y == 0):
        print(f"Il numero {x} è divisibile per {y}")
        return True

    else:
        print(f"Il numero {x} non è divisibile per {y}")
        return False

def main():

    # Prima parte
    x = int(input("Inserisci un numero intero: "))
    check_if_divisible(x, 2)
    check_if_divisible(x, 3)
    check_if_divisible(x, 5)
    check_if_divisible(x, 7)

    # Seconda parte
    y = int(input("Inserisci il primo numero intero: "))
    z = int(input("Inserisci il secondo numero intero: "))
    check_if_divisible(y, z)

    return

if __name__ == "__main__":
    main()