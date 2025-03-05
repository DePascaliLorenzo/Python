"""
I. Crea uno script nominandolo “esercizio_09”
II. Richiedi all'utente di inserire un valore numerico intero positivo
III. Calcola il fattoriale del numero inserito
OUTPUT Stampa in console il fattoriale del numero inserito
"""

intero = int(input("Inserisci un valore numerico intero positivo: "))
contatore = intero

while contatore > 1:
    contatore -= 1
    intero *= contatore

print(f"Il fattoriale è {intero}")