from object_oriented.principi.model.persona import Persona

# definizione classe Studente
class Studente(Persona):

    # metodo di inizializzazione
    def __init__(self, nome, cognome, eta, media_voti):
        super().__init__(nome, cognome, eta)
        self.media_voti = media_voti

    # metodo di istanza  per funzionalità specifica
    def annotazione_appunti(self):
        print(f'{self.nome} sta prendendo appunti')