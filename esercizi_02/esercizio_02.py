"""
I. Crea uno script nominandolo “esercizio_02”
II. Richiedi in input all'utente due numeri interi positivi
III. Controlla che il secondo numero inserito sia maggiore del primo e, sino a quando
tale condizione non si verifica, continua a richiedere all'utente l'inserimento del
secondo numero
OUTPUT
Stampa in console i soli numeri pari compresi nell'intervallo tra il 1° ed il 2° numero
ricevuti in input (compresi)
"""

numero1 = int(input("Inserisci il primo numero intero positivo: "))
numero2 = int(input("Inserisci il secondo numero intero positivo: "))

while numero2 < numero1:
    numero2 = int(input("Inserisci il secondo numero intero positivo: "))

lista_numeri_pari = []

for contatore in range(numero1, numero2 + 1):
    if contatore % 2 == 0:
        lista_numeri_pari.append(contatore)

print(lista_numeri_pari)