"""
Realizzare, in stile Object Oriented, un'applicazione che consenta, mediante input console,
la gestione di un catalogo prodotti e rispetti i seguenti requisiti:
I. Ogni prodotto sarà rappresentato da nome e prezzo.
II. L'applicazione deve poter gestire tutte le possibili eccezioni dovute ad input
erronei o mancanti.
III. L'applicazione deve offrire la possibilità di registrare nuovi prodotti e visualizzare,
in qualunque momento, l'intero catalogo.
"""
class Prodotto: # nomi delle classi sempre al singolare e con l'iniziale maiuscola

    # attributo di classe -> raggruppamento oggetti Smartphone
    catalogo = []

    # metodo di inizializzazione. Serve per definire struttura degli oggetti e costruirli
    def __init__(self, nome = None, prezzo = None):
        self.nome = nome
        self.prezzo = prezzo

    # metodo di istanza -> funzionalità di rappresentazione testuale in struttura (riscritto)
    def __repr__(self):
        return f'{self.nome} - {self.prezzo}€'

    # metodo di classe -> popolamento catalogo
    @classmethod
    def popolamento_catalogo(cls, *args):
        for prodotto in args:
            cls.catalogo.append(prodotto)

print(Prodotto.catalogo)

while True:
    nome_prodotto = input('Indica il nome del tuo nuovo prodotto (Oppure 0 per uscire): ')
    if nome_prodotto == "0":
        print('Hai deciso di uscire')
        print(Prodotto.catalogo)
        exit(4)
    else:
        try:
            prezzo_prodotto = input('Indica il prezzo del nuovo prodotto: ')
            prezzo_prodotto = float(prezzo_prodotto.strip().replace(',','.'))
            nuovo_prodotto = Prodotto(nome_prodotto, prezzo_prodotto)
            Prodotto.popolamento_catalogo(nuovo_prodotto)
            print(Prodotto.catalogo)
        except ValueError as e:
            print('errore')