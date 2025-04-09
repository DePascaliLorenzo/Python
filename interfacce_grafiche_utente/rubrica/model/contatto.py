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

    # metodo per verificare quando 2 contatti sono uguali
    def __eq__(self, other):
        if isinstance(other, Contatto):
            return (self.nome == other. nome and self.cognome == other.cognome and self.telefono == other.telefono)
        return False

    # metodo di istanza per serializzazione (Contatto -> dict)
    def serializzazione(self):
        return self.__dict__
