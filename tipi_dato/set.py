# dichiarazione e istanziazione set

# set_uno = {1, "ciao", True, (1,2,3), [1,2,3]}
# errore, un set non può contenere elementi mutabili
set_due = {1, 'ciao', True, (1, 2, 3)}
print(set_due, type(set_due))
set_tre = set([1, 3, 3, 4, 4, 2])
print(set_tre, type(set_tre))
set_vuoto_uno = set()  # set vuoto con constructor
print(set_vuoto_uno, type(set_vuoto_uno))
set_vuoto_due = {}  # dizionario vuoto
print(set_vuoto_due, type(set_vuoto_due))

# aggiunta e rimozione elementi set

set_vuoto_uno.add(34)
print(set_vuoto_uno)
set_due.add('ciao')
print(set_due)
set_due.remove(1) # rimuove l'elemento con valore 1
print(set_due)