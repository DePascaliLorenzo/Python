from functools import reduce

# definizione di una lista di numeri
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ottenimento di una nuova lista con numeri di quella originale
lista_raddoppiati = list(map(lambda x: x*2, lista))
print(lista_raddoppiati)

print()

# ottenimento di una nuova lista con i soli numeri dispari della lista originale
lista_dispari = list(filter(lambda x: x % 2 != 0, lista))
print(lista_dispari)

print()
# ottenimento del prodotto generale della lista
prodotto = reduce(lambda x, y: x * y, lista)
print(prodotto)