from negozio import Negozio
from cliente import Cliente
import threading

# istanziazione oggetto Negozio (comune a tutti i clienti thread)
negozio = Negozio()

# lista locale per creazione e avvio thread cliente
clienti = [Cliente(nome, negozio) for nome in ['Laura', 'Mario', 'Gianni', 'Sara', 'Davide']]

# popolamento lista attesa ufficiale
Cliente.lista_attesa.extend(clienti)

# apertura negozio
print('Clienti in attesa: ', Cliente.lista_attesa)
for cliente in clienti:
    cliente.start()