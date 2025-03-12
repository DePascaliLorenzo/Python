from object_oriented.full_oo.model.dispositivo import Dispositivo
from object_oriented.full_oo.model.telefono import Telefono

# definizione sottoclasse concreta Cordless
class Cordless(Telefono, Dispositivo):

    # metodo di inizializzazione
    def __init__(self, durata_batteria, raggio_azione):
        super().__init__(durata_batteria)
        self.raggio_azione = raggio_azione

    # override obbligatorio metodo astratto di superclasse Telefono
    def connessione(self):
        print('Collega alla presa telefonica')

    # override obbligatorio metodo astratto di superclasse Dispositivo
    def inizializzazione_dispositivo(self):
        print('Inserisci numero di telefono')

    # override metodo di rappresentazione testuale per riscrittura completa
    def __repr__(self):
        return f'Linea Telefoni - Durata Batteria: {self.durata_batteria} - Raggio d\'azione: {self.raggio_azione}'