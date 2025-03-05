"""
I. Crea uno script nominandolo “esercizio_05”
II. Richiedi all'utente di inserire un valore numerico intero positivo
III. Verifica se il numero inserito è un “numero primo” oppure no
OUTPUT
Stampa in console un opportuno messaggio all'utente
"""
primo = False

valore_numerico = int(input("Inserisci un numero intero >>> "))
if valore_numerico > 1:
    primo = True
    for i in  range (2,valore_numerico):
        if valore_numerico % i == 0:
            primo = False
            break

if primo:
    print(f"{valore_numerico} è un numero primo.")
else:
    print(f"{valore_numerico} NON è un numero primo.")