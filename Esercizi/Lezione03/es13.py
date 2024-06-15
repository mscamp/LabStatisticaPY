"""
    ESERCIZIO 3.13
    Calcola la probabilità che dieci campionamenti di una distribuzione gaussiana cadano nell'intervallo centrato sulla media della distribuzione di larghezza pari
    ad una deviazione standard.
"""

# Librerie
from scipy.stats import norm

def main():

    # Parametri gaussiana
    media = 0.0
    devstd = 1.0

    # Definizione della pdf
    gauss = norm(media, devstd)
    
    # Calcolo della probabilità per il singolo evento
    prob_sing = gauss.cdf(media + devstd) - gauss.cdf(media - devstd)

    # Calcolo probabilità congiunta
    prob_joint = prob_sing ** 10

    # Stampa a schermo il risultato
    print(f"Probabilità che 10 eventi cadano in media +/- sigma: {prob_joint}")

    return

if __name__ == "__main__":
    main()