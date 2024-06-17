"""
    ESERCIZIO 4.3
    Mostra che, prendendo come seed un numero pseudo-casuale appartenente ad una sequenza generata da un generatore lineare 
    congruenziale di interi si ottiene la stessa sequenza a partire da quel numero.
"""

def generatore_lineare_congruenziale(x: int, M: int, A: int, C: int) -> int:
    return (A * x + C) % M

def main() -> None:

    # Parametri
    M: int = 2147483647
    A: int = 214013
    C: int = 2531011

    # Variabili
    x_0: int = 14 # seed
    sequence_1: list[int] = [x_0]
    sequence_2: list[int] = []
    sequence_3: list[int] = []

    # Genera la prima sequenza di numeri pseudo-casuali
    print("--- SEQUENZA 1 ---")
    print(f"Seed: {x_0}")

    for i in range(10):
        sequence_1.append(generatore_lineare_congruenziale(sequence_1[i], M, A, C))
        print(f"Elemento {i + 1}: {sequence_1[-1]}")
    
    print('\n')
    
    # Genera la seconda sequenza di numeri pseudo-casuali
    print("--- SEQUENZA 2 ---")
    print(f"Seed: {sequence_1[3]}")

    sequence_2.append(sequence_1[3])

    for i in range(10):
        sequence_2.append(generatore_lineare_congruenziale(sequence_2[i], M, A, C))
        print(f"Elemento {i + 1}: {sequence_2[-1]}")
    
    print('\n')
    
    # Genera la terza sequenza di numeri pseudo-casuali
    print("--- SEQUENZA 3 ---")
    print(f"Seed: {sequence_2[4]}")

    sequence_3.append(sequence_2[4])

    for i in range(10):
        sequence_3.append(generatore_lineare_congruenziale(sequence_3[i], M, A, C))
        print(f"Elemento {i + 1}: {sequence_3[-1]}")
    
    print('\n')

    return

if __name__ == "__main__":
    main()