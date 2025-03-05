"""
I. Crea uno script nominandolo “esercizio_01”
II. Dichiara e istanzia una lista popolata con i seguenti elementi:
 “questa”, ”è”, ”la”, ”mia”, ”prima”, ”lista”
OUTPUT
Utilizzando un costrutto iterativo a tua scelta, stampa in console ogni singolo elemento
della lista in ordine inverso rispetto a quello di popolamento
"""

lista = ["questa", "è", "la", "mia", "prima", "lista"]

for contatore in range(len(lista) - 1, -1, -1):
    print(lista[contatore])