class Contatto:

    def __init__(self, nome = None, cognome = None, telefono = None):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono

    def __repr__(self):
        return f'{self.nome} {self.cognome} - Telefono: {self.telefono}'

    # metodo di classe per la deserializzazione (dict -> Contatto)
    @classmethod
    def deserializzazione(cls, dizionario):
        return cls(**dizionario)

    # metodo di istanza per conversione Contatto -> list
    def lista_attributi(self):
        return self.nome,self.cognome,self.telefono
