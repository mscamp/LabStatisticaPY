"""
    ESERCIZIO 4.8 (da risolvere dopo aver seguito la lezione 5)
    Implementa un oggetto chiamato 'stats', che calcoli le statistiche associate ad un campione di numeri in una lista.
"""

# Librerie
import numpy as np

class Stats:

    # Costruttore
    def __init__(self, sample):
        self.sample = sample
        self.sums = sum(self.sample)
        self.sumsq = sum([x**2 for x in self.sample])
        self.size = len(self.sample)

    # Metodi
    def mean(self):
        return self.sums / self.size
    
    def var(self, bessel = True):

        if bessel:
            return self.sumsq / (self.size - 1)

        else:
            return self.sumsq / self.size

    def std(self, bessel = True):
        return np.sqrt(self.var(bessel))

    def std_mean(self, bessel = True):
        return self.std(bessel) / np.sqrt(self.size)

    def append(self, element):

        self.sample.append(element)
        self.sums += element
        self.sumsq += element**2
        self.size += 1

        return