# dichiarazione e istanziazione di liste vuote
lista_uno =[] # literal
print(lista_uno, type(lista_uno))
lista_due = list() # mediante costruttore di classe list
print(lista_due, type(lista_due))

print()

# popolamento delle liste
lista_uno.append(10) # aggiunge il valore 10 alla lista
lista_uno.append(20) # aggiunge il valore 20 alla lista
print(lista_uno, len(lista_uno)) # stampa la lista e la sua lunghezza
lista_uno.insert(1,34) # inserisce il valore 34 nella posizione 1
print(lista_uno, len(lista_uno))

print()

# dichiarazione, istanziazione e popolamento
lista_tre = [3, 5, "ciao", False] # literal
lista_quattro = list((4, 10, "bello", 10)) # mediante costruttore di classe list (con tupla)
print(lista_tre, len(lista_tre))
print(lista_quattro, len(lista_quattro))
lista_quattro.append(4 < 8) # aggiunge il valore True alla lista
print(lista_quattro, len(lista_quattro))

print()

# accesso a elementi in una lista (in base a indice posizionale)
print(lista_tre[2]) # stampa l'elemento in posizione 2 (errore se non esiste)
print(lista_tre[0]) # stampa l'elemento in posizione 0 (errore se vuota)
print(lista_tre[-1]) # stampa l'ultimo elemento della lista (errore se lista vuota)

print()

# modifica di elementi presenti nella lista
lista_quattro[1] = True # modifica l'elemento in posizione 1
print(lista_quattro)

print()

# rimozione di elementi presenti in lista
lista_quattro.remove(10) # rimuove la prima occorrenza del valore 10
print(lista_quattro)

print()

# concatenazione di liste
lista_uno += lista_tre # concatenazione di liste
print(lista_uno)

print()

# raddoppio degli elementi di una lista
lista_uno *= 2 # raddoppio degli elementi di una lista
print(lista_uno)

print()

# operazione di slicing
print(lista_uno[3:]) # sda indice inzio compreso a fine naturale
print(lista_uno[:4]) # da inizio naturale a indice fine escluso
print(lista_uno[2:5]) # da indice inizio compreso a indice fine escluso

print()

# principali metodi di classe list
lista_uno.reverse() # inverte l'ordine degli elementi
print(lista_uno)
# lista_uno.sort() commentato per errore di ordinamento su lista etereogenea
# print(lista_uno)
lista_cinque = [45, 5, 78, 3]
lista_cinque.sort()
print(lista_cinque)

print()

lista_sei = [45, 5, 78, 3]
lista_sei.sort(reverse = True)
print(lista_sei)

print()

# unpackaging di liste
lista_sette = ['ciao', True]
uno, due = lista_sette
print(uno, type(uno))
print(due, type(due))
print(lista_sette)

print()

# scomposizione di una stringa in una lista (in base ad un cararttere separatore)

stringa = 'uno,due,tre'
lista_otto = stringa.split(',')
print(lista_otto)
stringa = " ".join(lista_otto)
print(stringa)

print()
