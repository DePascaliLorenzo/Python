"""
Partire da una lista vuota e popolarla di 10 valori numerici interi pseudo-casuali
- 1^ lista dove ci potranno essere dei duplicati
- 2^ lista senza duplicati
"""
import random

# lista vuota che ospiterà i numeri casuali
lista = []

# ciclo di popolamento
for _ in range(10):
    casuale = random.randint(1, 10) # minimo e massimo inclusi
    lista.append(casuale)

# stampa della lista popolata
print(lista)

# pulizia lista
lista.clear()

# popolamento lista senza duplicati

while len(lista) < 10:
    casuale = random.randint(1, 10)
    if casuale in lista:
        continue
    lista.append(casuale)

print(lista)