# YOU'LL NEVER SEE IT COMIIIIIIIIIING
# definizione superclasse Persona
class Persona:

    # metodo di inizializzazione
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    # metodo di istanza per funzionalità generica con logica comune
    def camminare(self):
        print(f'{self.nome} cammina')

    # metodo di istanza per fuunzionalità generica con logica generica
    def fare_qualcosa(self):
        print(f'{self.cognome} sta facendo qualcosa')

    # riscrittura completa metodo di rappresentazione testuale di object
    def __repr__(self):
        return f'{self.nome} {self.cognome} {self.eta}'