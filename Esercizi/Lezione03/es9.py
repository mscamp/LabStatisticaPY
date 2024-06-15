"""
    ESERCIZIO 3.9
    Usa l'oggetto scipy.stat.norm per determinare l'area delle code di una distribuzione normale, fuori dall'intervallo individuato da 1, 2, 3, 4 e 5 deviazioni
    standard attorno alla sua media.
"""

# Librerie
from scipy.stats import norm
from scipy.integrate import quad

def main():

    # Variabili
    integrali = []
    errori_integrali = []

    # Parametri della PDF
    media = 0.0
    devstd = 1.5
    norm_fixed = norm(media, devstd)

    # Calcolo delle aree
    for i in range(1, 6):
        estremo = i * devstd
        integrali.append(1.0 - quad(norm_fixed.pdf, -estremo, estremo)[0])
        errori_integrali.append(quad(norm_fixed.pdf, -estremo, estremo)[1])

    # Stampa a schermo
    for i in range(0, 5):
        print(f"{i + 1} sigma: {integrali[i]} +/- {errori_integrali[i]}")

    return

if __name__ == "__main__":
    main()