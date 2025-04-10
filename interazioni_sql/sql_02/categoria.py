class Categoria:

    def __init__(self, id = None, descrizione = None):
        self.id = id
        self.descrizione = descrizione

    def __repr__(self):
        return (f'Categoria - id: {self.id} - descrizione: {self.descrizione}')

    # metodo di rappresentazione testuale specifico per inclusione in Articolo
    def stampa_per_articolo(self):
        return self.descrizione
