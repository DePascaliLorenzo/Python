# Dobbiamo stampare 10 volte la frase "Ciao mondo!" tenendo il conteggio delle iterazioni.

for contatore in range(10):
    print(f"Ciao mondo! {contatore}") # stampa la stringa 10 volte

print('\n')

# Dobbiamo stampare 10 volte la frase "Ciao mondo!" tenendo il conteggio delle iterazioni (1-10).
for contatore in range(1,11):
    print(f"Ciao mondo! -> a questo giro il contatore vale {contatore}") # stampa la stringa 10 volte

print ('\n')

# Iteriamo gli elementi di una lista per stamparli
lista = ['uno', 'due', 'tre', 'quattro']
for elemento in lista:
    print(elemento)

print("\n")

# iteriamo gli elementi di una lista per stampare solo quelli con indice pari
for indice in range(0, len(lista), 2):
    print(lista[indice])

print('\n')

# iteriamo gli elementi di una lista dall'ultimo al primo
for indice in range(len(lista)-1, -1, -1):
    print(lista[indice])

print('\n')

# iteriamo gli elementi di una lista dall'ultimo al primo (iterazione inversa) con slicing lista
for elemento in lista[::-1]:
    print(elemento)

print('\n')

# abbiamo una lista di numeri e li vogliamo stampare ma se nella lista c'è il numero 5 fermiamo il ciclo
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeri:
    if numero == 5:
        break
    print(numero)
else:
    print("Il ciclo ha terminato il suo lavoro")

print('\n')

# abbiamo una lista di numeri e li vogliamo stampare ma se nella lista c'è il numero 5 saltiamo la stampa di quel numero
for numero in numeri:
    if numero == 5:
        continue
    print(numero)
else:
    print("Il ciclo ha terminato il suo lavoro")

print("Il programma è finito")