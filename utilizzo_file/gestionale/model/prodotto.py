# definizione classe di modellazione oggetto logico prodotto con struttura conforme al file di archiviazione
class Prodotto:

    # metodo di inizializzazione
    def __init__(self, id = None, tipologia = None, marca = None, modello = None, prezzo = None):
        self.id = id
        self.tipologia = tipologia
        self.marca = marca
        self.modello = modello
        self.prezzo = prezzo

    # metodo di rappresentazione testuale
    def __repr__(self):
        return (f'Id Prodotto: {self.id} - Tipologia: {self.tipologia}'
                f'\nMarca: {self.marca} - Modello: {self.modello}'
                f'\nPrezzo: {self.prezzo}€\n---------------------------------------------------------')

    # metodo di rappresentazione in formato lista
    def to_list(self):
        return[self.id,self.tipologia,self.marca,self.marca,self.prezzo]