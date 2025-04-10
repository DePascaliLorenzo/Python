class Articolo:

    def __init__(self, id = None, nome = None, prezzo = None, categoria = None):
        self.id = id
        self.nome = nome
        self.prezzo = prezzo
        self.categoria = categoria # gestione relazione molti a uno (N:1)


    def __repr__(self):
        return f'Articolo {self.id} ({self.categoria.stampa_per_articolo()}) - {self.nome}, {self.prezzo} €'

    # metodo di rappresentazione testuale specifico per inclusione in Categoria
    def stampa_per_categoria(self):
        return f'{self.id} - {self.nome}, {self.prezzo:.2f} €'
