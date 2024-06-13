""" 
    ESERCIZIO 2.1
    Crea array NumPy 1-dimensionali in modi differenti
"""

# Librerie
import numpy as np

def main():

    # Variabili
    python_list = [1, 2, 3, 4]
    array_1 = np.array(python_list)
    array_2 = np.zeros(4)
    array_3 = np.ones(4)
    array_4 = np.arange(1, 5)
    array_5 = np.linspace(0, 1, 100)
    array_6 = np.empty(4)

    # Stampa a schermo gli array
    print(array_1)
    print(array_2)
    print(array_3)
    print(array_4)
    print(array_5)
    print(array_6)

    return

if __name__ == "__main__":
    main()