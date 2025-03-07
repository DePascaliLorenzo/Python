# definizio di una funzione di pura esecuzione (non restituisce nulla)
def stampa_saluto():
    print("Ciao a tutti")

# definizione di una funzione che restituisce un oggetto
def torna_saluto():
    return "Ciao a tutti"

# definizione di una funzione che accetta un parametro ed esegue un'istruzione

def salutami(nome):
    print(f"Ciao {nome}")

# definizione di una funzione che accetta due parametri e ritorna un valore
def concatena(a, b):
    return a + b

# definizione di una funzione che accetta due parametri e ritorna un valore
def concatena_due(a, b):
    return str(a) + str(b)

# definizione di una funzione che accetta tre parametri (di cui uno faocltativo) e ritorna un valore
def somma(a, b, c=0):
    return a + b + c

# definizione di una funzione che accetta due parametri e ritorna un valore
def concatena_tre(a, b):
    return a + str(b)

# definizione di una funzione che accetta tre parametri facoltativi e ritorna un valore
def somma_due(a=0, b=0, c=0):
    return a + b + c

# definizione di una funzione che accetta n parametri ed esegue un'istruzione
def itera(*args):
    print(args, type(args))
    for elemento in args:
        print(elemento)

# definizione di una funzione che accetta n parametri nominali
def stampa(**kwargs):
    print(kwargs, type(kwargs))
    for chiave, valore in kwargs.items():
        print(f"{chiave}: {valore}")

# INVOCAZIONE FUNZIONE
stampa_saluto()
saluto = torna_saluto()
print(torna_saluto())
salutami("Lorenzo")
print(concatena("Ciao", "Mondo"))
print(concatena(1, 5))
# print(concatena_due("Ciao", 5)) # darebbe errore in quanto non posso concatenare stringa con intero
print(somma(1, 2))
print(concatena_tre(b=5, a="Ciao"))
print(somma_due())
itera(1, 4, 6, 7)
itera('ciao', 'mondo')
stampa(nome='Mario', cognome='Rossi', età=30)