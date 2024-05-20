"""
    ESERCIZIO 1.7
    Scrivi un programma che risolva le equazioni di secondo grado ax^2 + bx + c = 0
"""

# Librerie
from math import sqrt

def second_order_eq_solver(a, b, c):
    """ Riceve come argomenti i coefficienti dell'equazione (float) e restituisce una tuple contenente le due soluzioni """

    # Variabili 
    delta = (b**2 - 4*a*c)

    # Controlla se delta < 0
    if delta < 0:
        print("Il delta deve essere non negativo. Riprova.")
        return None

    else:
        sol1 = (-b + sqrt(delta))/(2*a)
        sol2 = (-b - sqrt(delta))/(2*a)

        return [sol1, sol2]

def main():

    # Inserimento coefficienti
    print("--- RISOLUZIONE DI ax^2 + bx + c = 0 ---")
    a = float(input("Inserisci coefficiente a: "))
    b = float(input("Inserisci coefficiente b: "))
    c = float(input("Inserisci coefficiente c: "))

    # Soluzioni
    solutions = second_order_eq_solver(a, b, c)

    # Stampa a schermo le soluzioni
    if solutions != None:
        print(f"Soluzioni: \n x1 = {solutions[0]} \n x2 = {solutions[1]}")

    else:
        exit(1)

    return

if __name__ == "__main__":
    main()