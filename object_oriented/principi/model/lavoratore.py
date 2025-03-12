from object_oriented.principi.model.persona import Persona

# definizione classe Lavoratore
class Lavoratore(Persona):

    # metodo di inizializzazione
    def __init__(self, nome, cognome, eta, reddito):
        super().__init__(nome, cognome, eta)
        self.reddito = reddito

    # se, all'interno dell'ambito della classe, si fa TASTO DESTRO -> GENERATE possiamo scrivere automaticamente gli ovveride method
    # come __init__

    def __repr__(self):
        return f'{self.nome}{self.cognome} - {self.cognome} (Lavoratore) {self.reddito}'

    # metodo di istanza per funzionalità specifica di un lavoratore
    def richiesta_permesso(self):
        print(f'{self.cognome} chiede un permesso')

    #override motodo di superclasse per riscrittura print
    def fare_qualcosa(self):
        print(f'{self.cognome} lavora')