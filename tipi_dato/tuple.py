# dichiarazione e istanziazione di una tupla
tupla_uno = 1, 2, ['ciao','mondo'], True, 'bello' # literal
print(tupla_uno, type(tupla_uno))
tupla_due = tuple([1, 2, 3, 4]) # constructor, le parentesi tonde sono opzionali
print(tupla_due, type(tupla_due))

# tupla_tre = tuple(1) # errore, non è una tupla

tupla_quattro = tuple("ciao")
print(tupla_quattro, type(tupla_quattro))
tupla_cinque = 1, # tupla con un solo elemento
print(tupla_cinque, type(tupla_cinque))
tupla_vuota_uno = () # tupla vuota
tupla_vuota_due = tuple() # tupla vuota

# accesso elementi
print(tupla_uno[2]) # 1
print(len(tupla_uno), len(tupla_vuota_uno))

# slicing su tuple

tupla_sei = tupla_uno[1:4]
print(tupla_sei)

# unpackaging

a, b, c = tupla_sei
print(a, b, c)