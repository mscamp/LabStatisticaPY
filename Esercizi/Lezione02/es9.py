"""
    ESERCIZIO 2.9
    Scrivi un programma che plotti l'insieme di Mandelbrot usando MatPlotLib
"""

# Librerie
import numpy as np
from matplotlib import pyplot as plt

def convergenza(c, n = 100):
    
    # Variabili
    z = complex(0.0)

    for i in range(n):
        z = z**2 + c

        if abs(z) > 2:
            return False

    return True        

def main():

    # Estremi del dominio
    xmin = -2
    xmax = 1
    ymin = -2
    ymax = 2
    resolution = 0.03 

    # Definizione della regione di piano complesso
    x_coord = np.arange(xmin, xmax, resolution) 
    y_coord = np.arange(ymin, ymax, resolution) 

    # Plot
    fig, ax = plt.subplots (nrows = 1, ncols = 1)

    ix = 0
    for x in x_coord:
        iy = 0

        for y in y_coord:
            if convergenza(complex(x, y)):
                ax.plot(x, y, marker = "*", color = "black")

            else:   
                ax.plot(x, y, marker = "*", color = "white")

            iy = iy + 1
        ix = ix + 1

    # Salva il plot come file png
    fig.savefig('mandelbrot.png',dpi=300)
    plt.show()

    return

if __name__ == '__main__':
    main()