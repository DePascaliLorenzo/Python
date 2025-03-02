# dichiarazione e istanziazione di variabili per booleani
boolean_uno = True
boolean_due = False

print(boolean_uno, type(boolean_uno))
print(boolean_due, type(boolean_due))

# analisi logiche di verità
print(bool(-12), bool(0)) # True (tutti i numeri che non sono 0) - False (solo 0)
print(bool(" "), bool("")) # True (se la stringa non è vuota) - False (stringa vuota)
print(bool([]), bool([1,2])) # True se la lista ha dei valori al suo interno - False se la stringa è vuota
print(bool(None)) # False il valore è nullo

# operatori logici and e or
print(True and True) # una operazione AND è vera se TUTTE le sotto-espressioni è vere
print(True and False)

print(True or False) # una operazione OR è vera se UNA SOLA delle sotto-espressioni è vera

# espressioni con operatori di confronto

espressione_uno = 12 <= 10
print(espressione_uno, type(espressione_uno))
espressione_due = "ciao" == "ciao"
print(espressione_due, type(espressione_due))
espressione_tre = 10 != 10 and 1 < 3
print(espressione_tre, type(espressione_tre))
espressione_quattro = 10 != 10 or 1 < 3
print(espressione_quattro, type(espressione_quattro))

# operatore NOT

espressione_cinque = not(10 == 10)
print(espressione_cinque)

#operatore di identità IS

potenza_uno = 2 ** 1000
potenza_due = 2 ** 1000

print(potenza_uno == potenza_due) # == controlla il valore (True)
print(potenza_uno is potenza_due) # is controlla la locazione di memoria (False)
potenza_due = potenza_uno
print(potenza_uno is potenza_due)