class Prodotto:

    def __init__(self, nome, prezzo):
        if not isinstance(prezzo, (int, float)) or prezzo < 1:
            raise ValueError('Il prezzo deve essere un numero non inferiore di 1')
        self.nome = nome
        self.prezzo = prezzo + 1

