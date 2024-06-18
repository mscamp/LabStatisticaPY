"""
    ESERCIZIO 4.2 (da risolvere dopo aver seguito la lezione 5)
    Implementa il generatore lineare congruenziale come oggetto che contenga un metodo per generare un numero pseudo-casuale e un 
    metodo per impostare il seed, usando un'appropriata variabile della classe per immagazzinare questa informazione. Come dovrebbe
    cambiare il seed ogni qualvolta un numero pseudo-casuale viene generato?
"""

# Librerie
from random import random

class LinearGenerator:
    """ Generatore lineare congruenziale """

    def __init__(self, M, A, C):
        
        # Controlli sui valori passati
        if M <= 0:
            raise ValueError("M deve essere maggiore di 0")
        
        if not(0 < A < M):
            raise ValueError("A deve essere strettamente compreso tra 0 e M")

        if type(M) != int or type(A) != int or type(C) != int: 
            raise TypeError("I valori passati devono essere interi")

        # Membri
        self.M = M
        self.A = A
        self.C = C

    # Metodi
    def set_seed(self, seed):
        
        if type(seed) != int:
            raise TypeError("Il seed deve essere un intero")

        if not(0 < seed < self.M):
            raise ValueError("Il seed deve essere strettamente compreso tra 0 e M")

        self.num = seed

        return

    def gen(self):
        self.num = (self.A * self.num + self.C) % self.M
        return self.num

def main():
    
    # Variabili
    N = 10 # numero di elementi della sequenza
    M =  2147483647
    A =  214013
    C =  2531011
    seed = 5741206

    # Generatore lineare congruenziale
    generator = LinearGenerator(M, A, C)
    generator.set_seed(seed)
    
    # Sequenza di numeri casuali
    for i in range(N):
        print(f"Numero {i+1}: {generator.gen()}")

    return

if __name__ == "__main__":
    main()