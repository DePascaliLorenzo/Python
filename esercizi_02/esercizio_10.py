"""
I. Crea uno script nominandolo “esercizio_10”
II. Implementa un algoritmo che permetta di rappresentare i primi 20 numeri della sequenza di Fibonacci
OUTPUT Stampa in console la sequenza su un'unica riga
"""

sequenza = [0,1]
contatore = 0

while contatore < 20:
        print(sequenza[contatore], end=" ")
        sequenza.append(sequenza[contatore] + sequenza[contatore + 1])
        contatore += 1