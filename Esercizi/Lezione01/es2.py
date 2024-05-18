"""
    ESERCIZIO 1.2
    Scrivi un programma che, dati i tre lati di un triangolo, determini se il triangolo sia acutangolo,
    rettangolo o ottusangolo.
"""

# Librerie
from math import acos
from math import pi

def type_of_triangle(x, y, z):
    """ Riceve come argomenti i tre lati di un triangolo e determina se esso sia acutangolo, rettangolo o ottusangolo. """

    # Determina gli angoli (teorema del coseno)
    b = acos((x**2 + y**2 - z**2)/(2*x*y))
    a = (y / z) * b
    c = (x / z) * b  

    # Determina il tipo di triangolo
    if (a == (pi / 2)) or (b == (pi / 2)) or (c == (pi / 2)):
        print("Il triangolo è rettangolo.")

    elif (a < (pi / 2)) and (b < (pi / 2)) and (c == (pi / 2)):
        print("Il triangolo è acutangolo.")

    elif (a > (pi / 2)) or (b > (pi / 2)) or (c > (pi / 2)):
        print("Il triangolo è ottusangolo.")

    else:
        print("I dati inseriti non sono validi. Riprova.")

    return

def main():
    # Variabili
    lato_1 = float(input("Inserire il primo lato: ")) 
    lato_2 = float(input("Inserire il secondo lato: ")) 
    lato_3 = float(input("Inserire il terzo lato (maggiore degli altri due): ")) 

    # Determina il tipo di triangolo
    type_of_triangle(lato_1, lato_2, lato_3)

    return

if __name__ == "__main__":
    main()