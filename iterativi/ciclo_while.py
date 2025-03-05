# FORZATURA UTILIZZO CICLO WHILE COME CICLO FOR
# dobbiamo stampare 10 volte la frase Ciao Mondo tenendo il conteggio delle iterazioni (0-9)
contatore = 0
while contatore < 10:
    print(f"Ciao mondo! Il contatore ha attualmente valore: {contatore}")
    contatore += 1

print('\n')

# UTILIZZO IN AMBITO CORRETTO: ITERAZIONI NON DEFINITE
"""
Programma che permetta ad un utente di inserire numeri in input e, solo quando vuole l'utente, stampare la somma
dei numeri stessi
"""

# variabile per registrare la somma dei numeri
somma = 0

# ciclo di acquisizione input utente (tutti quelli che vuole lui)
while True:
    # acquisizione input utente
    numero = input('Digita un numero (oppure 0 per terminare): ')
    # validazione input
    if not numero.isnumeric():
        print('Questo non è un numero')
        continue
    # clausola uscita dal programma
    if numero == '0':
        break
    # conversione sicura del valore numerico
    numero = int(numero)
    # somma aritmetica
    somma += numero

# output finale presentato all'utente quando vuole terminare il programma
print(f'La somma dei numeri che hai inserito è: {somma}')