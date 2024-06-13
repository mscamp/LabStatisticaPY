"""
    ESERCIZIO 2.8
    Scrivi un programma che plotti il grafico delle funzioni trigonometriche fondamentali su un dominio
    opportuno, usando le universal functions di NumPy
    * Mostra che sin(x) e cos(x) differiscono di una fase
    * Mostra che i termini A e B nell'equazione f(x) = sin(x - A) + B rappresentano rispettivamente 
    traslazioni orizzontali e verticali della funzione
    * Mostra che i termini C e D nell'equazione g(x) = D * cos(Cx) rappresentano rispettivamente dilatazioni
    orizzontali e verticali della funzione
"""

# Librerie
import numpy as np
from matplotlib import pyplot as plt

def f(x, A, B):
    return np.sin(x - A) + B

def g(x, C, D):
    return D * np.cos(C*x)

def main():

    # Punti
    x_coord = np.linspace(0, 2 * np.pi, 10000)
    y_coord_1 = np.sin(x_coord)
    y_coord_2 = np.cos(x_coord)

    # Confronto funzioni trigonometriche
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.plot(x_coord, y_coord_1, label="sin(x)")
    ax.plot(x_coord, y_coord_2, label="cos(x)")
    ax.set_title("Funzioni trigonometriche", size = 14)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    plt.show()

    # Traslazioni di f
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    
    y_riferimento_traslazione = f(x_coord, 0, 0)
    y_traslazione_verticale = f(x_coord, 0, 1)
    y_traslazione_orizzontale = f(x_coord, 1, 0)

    ax.plot(x_coord, y_riferimento_traslazione, label="sin(x)")
    ax.plot(x_coord, y_traslazione_verticale, label="f_vert(x)")
    ax.plot(x_coord, y_traslazione_orizzontale, label="f_hor(x)")
    ax.set_title("Traslazioni di f", size = 14)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    plt.show()

    # Dilatazioni di g
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    
    y_riferimento_dilatazione = g(x_coord, 1, 1)
    y_dilatazione_verticale = g(x_coord, 1, 2)
    y_dilatazione_orizzontale = g(x_coord, 2, 1)

    ax.plot(x_coord, y_riferimento_dilatazione, label="cos(x)")
    ax.plot(x_coord, y_dilatazione_verticale, label="f_vert(x)")
    ax.plot(x_coord, y_dilatazione_orizzontale, label="f_hor(x)")
    ax.set_title("Dilatazioni di f", size = 14)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    plt.show()

    return

if __name__ == "__main__":
    main()