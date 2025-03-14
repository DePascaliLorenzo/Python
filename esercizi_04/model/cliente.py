class Cliente:

    def __init__(self, nome, cognome, numero_di_patente):
        self.nome = nome
        self.cognome = cognome
        self.numero_di_patente = numero_di_patente

    def __repr__(self):
        return f'Cliente - Nome: {self.nome} - Cognome: {self.cognome} - N° Patente: {self.numero_di_patente}'
