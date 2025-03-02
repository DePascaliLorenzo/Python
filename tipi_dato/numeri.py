import math

# dichiarazione e istanziazione di variabili per numeri interi
intero_uno = 10 # literal
print(intero_uno, type(intero_uno))
intero_due = int(19) # con costruttore di classe int
print(intero_due, type(intero_due))
intero_tre = int("22") # conversione stringa -> intero (se possibile, altrimenti crash)
print(intero_tre, type(intero_tre))
intero_quattro = int() # istanziazione di un intero con valore 0
print(intero_quattro, type(intero_quattro))

# dichiarazione e istanziazione di variabili per numeri decimali

decimal_uno = 13.7 # literal
print(decimal_uno, type(decimal_uno))
decimal_due = float(11.4) # con costruttore di classe float
print(decimal_due, type(decimal_due))
decimal_tre = float("420.69") #conversione stringa -> float (se possibile, altrimenti crash)
print(decimal_tre, type(decimal_tre))
decimal_quattro = float()
print(decimal_quattro)

# utilizzo operatore +

risultato_somma = intero_uno + decimal_uno
print(risultato_somma)

# utilizzo operatore /

risultato_divisione = intero_tre / intero_uno
print(risultato_divisione, type(risultato_divisione))

# utilizzo operatore // (divisione intera)

risultato_divisione_intera = intero_tre // intero_uno
print(risultato_divisione_intera, type(risultato_divisione_intera))

# utilizzo opratore // (divisione intera) con numeri decimali

risultato_divisione_intera_decimali = decimal_tre // decimal_uno
print(risultato_divisione_intera_decimali, type(risultato_divisione_intera_decimali))

# utilizzo operatore % (resto)

print(5 % 2)

# utilizzo operatore ** (elevazione a potenza)

print(5 ** 2)

# utilizzo funzione round, math.ceil

print(round(4.5)) # se la parte intera è pari, arrotonda per difetto se il decimale è .5
print(round(5.5)) # se la parte intera è dispari, arrotonda per eccesso se il decimale è .5
print(round(10.444572, 2))
print(math.ceil(10.123456)) # math.ceil arrotonda sempre per eccesso
print(math.floor(10.123456)) # math.floor arrotonda sempre per difetto

# i numeri sono oggetti immutabili

numero = 10
print(numero, id(numero))
numero = numero + 13
print(numero, id(numero))