"""
I. Crea uno script nominandolo “esercizio_03”
II. Utilizzando dei costrutti iterativi a tua scelta, crea una lista bidimensionale che
rappresenti una tabella composta da 2 righe e 3 colonne, popolata con valori
numerici interi casuali in range 50-100 (compresi)
OUTPUT
Utilizzando dei costrutti iterativi a tua scelta, stampa in console tutti gli elementi contenuti
nella struttura in formato tabellare
"""
import random

lista_2d = []

for indice_riga in range(2):
    riga = []
    for indice_colonna in range(3):
        riga.insert(indice_colonna, random.randint(50, 100))
    lista_2d.append(riga)

for indice in lista_2d:
    for indice_2 in indice:
        print("{:>4}".format(indice_2), end = " ")
    print()