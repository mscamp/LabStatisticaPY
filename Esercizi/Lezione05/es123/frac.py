"""
    ESERCIZIO 5.1
    Crea una libreria di Python che implementi la classe 'Fraction', contenente il suo costruttore, i membri in cui salvare numeratore
    e denominatore e il metodo della classe che restituisce il risultato della divisione tra numeratore e denominatore

    ESERCIZIO 5.2
    Implementa una funzione di test all'interno della libreria stessa, che verifichi che l'output di ciascun metodo della classe, e che
    stampi a schermo il valore del numeratore e del denominatore di una frazione

    ESERCIZIO 5.3
    Aggiungi alla classe Fraction l'overloading degli operatori +,-,*,/ in modo che ciascuna operazione restituisca un oggetto di tipo
    Fraction. Aggiungi alla funzione di test dell'esercizio precedente verifiche dei nuovi metodi definiti.

"""

# Librerie
from math import gcd

class Fraction:
    """ Classe che implementa le frazioni """

    # Costruttore
    def __init__(self, numerator: int, denominator:int ) -> None:

        # Controllo parametri
        if denominator == 0:
            raise ValueError("Il denominatore non può essere nullo")
        
        if type(numerator) != int:
            raise TypeError("Il numeratore deve essere un intero")
        
        if type(denominator) != int:
            raise TypeError("Il denominatore deve essere un intero")
        
        # Membri
        common_divisor: int = gcd(numerator, denominator)
        self.numerator: int = numerator // common_divisor # integer division with floor division
        self.denominator: int = int(denominator / common_divisor) # integer division with casting

        return

    # Metodi
    def show(self) -> None:
        """ Stampa la frazione a schermo """
        print(f"{self.numerator}/{self.denominator}")
        
    def print_value(self) -> None:
        print(f"{self.numerator/self.denominator}")

    def return_fraction(self) -> str:
        return (f"{self.numerator}/{self.denominator}")
        
    # Overloading di operatori
    def __add__(self, other):
        new_numerator: int = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator: int = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)
    
    def __sub__(self, other):
        new_numerator: int = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator: int = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)
    
    def __mul__(self, other):
        new_numerator: int = self.numerator * other.numerator
        new_denominator: int = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator: int = self.numerator * other.denominator
        new_denominator: int = self.denominator * other.numerator

        return Fraction(new_numerator, new_denominator)


def test() -> None:
    """ Test della classe Fraction """

    frac_1 = Fraction(3, 8)
    frac_2 = Fraction(2, 7)

    # Test metodi print
    frac_1.show()
    frac_1.print_value()

    frac_2.show()
    frac_2.print_value()

    # Esercizio 5.2
    print(f"Numeratore: {frac_1.numerator}")    
    print(f"Denominatore: {frac_1.denominator}")    
    print(f"Numeratore: {frac_2.numerator}")    
    print(f"Denominatore: {frac_2.denominator}")    

    # Esercizio 5.3
    frac_sum = frac_1 + frac_2
    frac_sub = frac_1 - frac_2
    frac_mul = frac_1 * frac_2
    frac_div = frac_1 / frac_2

    print(f"Somma: {frac_sum.return_fraction()}")
    print(f"Sottrazione: {frac_sub.return_fraction()}")
    print(f"Moltiplicazione: {frac_mul.return_fraction()}")
    print(f"Divisione: {frac_div.return_fraction()}")

    return

if __name__ == "__main__":
    test()