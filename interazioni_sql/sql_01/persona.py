class Persona:

    def __init__(self, id = None, nome = None, cognome = None, eta = None):
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def __repr__(self):
        return f'Persona n°{self.id} - Nome: {self.nome}, Cognome: {self.cognome}, Età: {self.eta}'