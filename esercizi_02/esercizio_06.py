"""
I. Crea uno script nominandolo “esercizio_06”
II. Utilizzando dei costrutti iterativi, crea un algoritmo per produrre l'output richiesto
OUTPUT Stampa in console della seguente rappresentazione:
X O X O X O X O X O
X O X O X O X O X O
X O X O X O X O X O
X O X O X O X O X O
X O X O X O X O X O
X O X O X O X O X O
X O X O X O X O X O
X O X O X O X O X O
X O X O X O X O X O
X O X O X O X O X O
"""

# Utilizzo di un costrutto iterativo per produrre l'output richiesto
for indice_riga in range(10):
    print("X O " * 5)