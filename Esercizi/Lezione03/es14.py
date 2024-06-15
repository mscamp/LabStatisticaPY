"""
    ESERCIZIO 3.14
    Calcola la probabilità che dieci campionamenti di una distribuzione poissoniana siano tutti maggiori della media della distribuzione.
"""

# Librerie
import numpy as np
from scipy.stats import poisson

def main():

    # Parametri poissoniana
    mu = 5.0

    # Definizione distribuzione
    poiss = poisson(mu)

    # Probabilità del singolo evento
    prob_sing = 1.0 - poiss.cdf(mu)

    # Probabilità congiunta
    prob_joint = prob_sing ** 10

    # Stampa a schermo il risultato
    print(f"Probabilità che 10 eventi cadano dopo la media mu: {prob_joint}")
    
    return

if __name__ == "__main__":
    main()