# definizione di una classe per modellazione ogetti Smartphone
class Smartphone: # nomi delle classi sempre al singolare e con l'iniziale maiuscola

    # attributo di classe -> raggruppamento oggetti Smartphone
    catalogo = []

    # metodo di inizializzazione. Serve per definire struttura degli oggetti e costruirli
    def __init__(self, marca = None, modello = None, dimensione_display = None, prezzo = None):
        self.marca = marca
        self.modello = modello
        self.dimensione_display = dimensione_display
        self.prezzo = prezzo

    # metodo di istanza -> funzionalità di invio chiamata
    def invio_chiamata(self, numero):
        print(f'Sono un {self.marca} e chiamo il numero {numero}')

    # metodo di istanza -> funzionalità di invio messaggio
    def invio_messaggio(self, destinatario):
        print(f'Sono un {self.marca} ({self.modello}) e invio un messaggio a: {destinatario}')

    # metodo di istanza -> funzionalità di rappresentazione testuale (riscritto)
    def __str__(self):
        return f'{self.marca} ({self.modello}) - display da {self.dimensione_display} pollici - prezzo {self.prezzo} €'

    # metodo di istanza -> funzionalità di rappresentazione testuale in struttura (riscritto)
    def __repr__(self):
        return f'{self.marca} ({self.modello}) - display da {self.dimensione_display} pollici - prezzo {self.prezzo} €'

    # metodo di classe -> popolamento catalogo
    @classmethod
    def popolamento_catalogo(cls, *args):
        for smartphone in args:
            cls.catalogo.append(smartphone)


# dichiarazione e istanziazione di 3 variabili a cui assegnare 3 oggeti di tipo Smartphone
smart_uno = Smartphone("NOKIA", "C-220", 5.57, 200.68)
smart_due = Smartphone('LG', 'A56', 6.6, 500.89)
smart_tre = Smartphone('MOTOROLA', 'L246', 4.99, 300.15)

# stampa oggetti
print(smart_uno, type(smart_uno))
print(smart_due, type(smart_due))
print(smart_tre, type(smart_tre))

# accesso in lettura dei parametri degli oggetti
print(smart_uno.prezzo)
print(smart_due.marca)
print(smart_tre.dimensione_display)

# accesso in scrittura dei parametri degli oggetti
smart_uno.prezzo = 300.55
print(smart_uno.prezzo)

# invocazione metodi di istanza
smart_uno.invio_chiamata('+39 111222333')
smart_due.invio_messaggio('Mario')

# aggiunta dei 3 Smartphone al catalogo
Smartphone.popolamento_catalogo(smart_uno, smart_due, smart_tre)
print(Smartphone.catalogo)

# dichiarazione e istanziazione di altri 2 Smartphone (senza conoscenza dei valori di alcuni attributi)
smart_quattro = Smartphone()
print(smart_quattro)
smart_quattro.prezzo = 500.78
print(smart_quattro)
smart_cinque = Smartphone (dimensione_display = 6.45)
print(smart_cinque)