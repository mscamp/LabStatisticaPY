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
    
    def skew(self):

        somma_scarti: float = 0.0

        for i in range(self.size):
            somma_scarti += (self.sample[i] - self.mean())**3

        somma_scarti /= self.size
        
        return somma_scarti / (self.std())**3

    def kurt(self):

        somma_scarti: float = 0.0
        
        for i in range(self.size):
            somma_scarti += (self.sample[i] - self.mean())**4

        somma_scarti /= self.size
        
        return (somma_scarti / (self.std())**4) - 3.0

    def append(self, element):

        self.sample.append(element)
        self.sums += element
        self.sumsq += element**2
        self.size += 1

        return