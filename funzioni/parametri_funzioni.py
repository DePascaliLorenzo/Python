# funzione che riceve un oggetto immutabili (stringhe, tuple, numeri)

def modifica_immutabile(ricevuto):
    ricevuto ="Buonasera"
    print(f'Nella funzione, ricevuto vale: {ricevuto}')

# funzione che riceve un oggetto mutabile (liste, dizionari, insiemi)
def modifica_mutabile(ricevuto):
    ricevuto[1] = 50
    print(f'Nella funzione, la lista contiene: {ricevuto}')

# INVOCAZIONE FUNZIONI
# gestione immutabile
saluto = "Buongiorno"
print(f'Dopo istanziazione, saluto vale: {saluto}') # Buongiorno
modifica_immutabile(saluto)
print(f'Dopo la funzione, saluto vale: {saluto}') # Buongiorno
# gestione mutabile
lista = [12, 10, 15, 78]
print(f'Dopo istanziazione, la lista contiene: {lista}') # [12, 10, 15, 78]
modifica_mutabile(lista)
print(f'Dopo la funzione, la lista contiene: {lista}') # [12, 50, 15, 78]
