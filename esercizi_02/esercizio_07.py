"""
Sviluppa un'applicazione secondo i seguenti criteri:
• Nel codice sorgente devi definire una costante istanziata con un valore numerico casuale in range 1-10 (compresi)
• Richiedi all'utente di inserire un numero intero compreso tra 1 e 10
• A questo punto:
◦ sino a quando, il numero inserito dall'utente, non è uguale al valore della variabile,
richiedigli un nuovo input informandolo ogni volta se, il numero da indovinare, è minore o maggiore di quello che ha appena inserito
◦ nel momento in cui, il numero inserito, risulta uguale al valore target,
invia all'utente un messaggio di congratulazioni
informandolo del numero di tentativi che sono stati necessari per indovinare
"""
import random

num_casuale = random.randint(1, 10)
uguale = False
tentativo = 0

while not uguale:
    num_input = int(input("Inserisci un numero compreso tra 1 e 10: "))
    if num_input == num_casuale:
        tentativo += 1
        print(f"Il numero è digitato è uguale a quello casuale. Hai azzeccato in {tentativo} tentativi")
        uguale = True
    elif num_input > 10:
        tentativo += 1
        print("Il numero digitato è maggiore di 10, digita un altro numero")
    elif num_input < 1:
        tentativo += 1
        print("Il numero digitato è minore di 1, digita un altro numero")
    elif num_input < num_casuale:
        tentativo += 1
        print("Il numero digitato è minore")
    elif num_input > num_casuale:
        tentativo += 1
        print("Il numero digitato è maggiore")
    else:
        tentativo += 1
        print("Ciò che hai digitato non è un numero")