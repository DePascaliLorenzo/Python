# dichiarazione e istanziazione di un dizionario

# dict_uno = {1:2, 2:'ciao', "ciao":[1,2,3,4], (1,2,3): True, [1,2]:"mondo"} commentato, le chiavi devono essere immutabili

dict_due = {1:2, 2:'ciao', "ciao":[1,2,3,4], (1,2,3): True, 1:"mondo"} # mantenuta unica chiave con ultimo valore
print(dict_due, type(dict_due))
dict_tre = dict(nome='Mario', cognome='Rossi', età=30) # constructor
print(dict_tre, type(dict_tre))
dict_quattro = {} # dizionario vuoto
dict_cinque = dict() # dizionario vuoto

print(dict_quattro)
print(dict_cinque)

# accesso elementi
print(dict_due['ciao'])

# unpackaging
a, b, c, d = dict_due
print(a, b, c, d)

# manipolazione dizionari
dict_due[4] = 'nuovo elemento'
print(dict_due)
dict_due[4] = 'nuovo elemento sovrascritto'
print(dict_due)
print(dict_due.pop(4))
print(dict_due)
print(dict_due.pop(4, 'elemento non presente'))