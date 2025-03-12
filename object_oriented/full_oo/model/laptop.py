from object_oriented.full_oo.model.computer import Computer
from object_oriented.full_oo.model.dispositivo import Dispositivo


# definizione sottoclasse concreta Laptop
class Laptop(Computer, Dispositivo):

    def __init__(self, sistema_operativo, schermo_touch):
        super().__init__(sistema_operativo)
        self.schermo_touch = schermo_touch

    # override obbligatorio metodo astratto superclasse Computer
    def sospensione_sistema(self):
        print('Chiudi lo schermo')

    # override obbligatorio metodo astratto superclasse Dispositivo
    def inizializzazione_dispositivo(self):
        print('Controlla carica batteria e configura account')

    # override metodo di rappresentazione testuale per riscrittura completa
    def __repr__(self):
        return f'Linea Computer - Sistema Operativo: {self.sistema_operativo} - Schermo Touch: {self.schermo_touch}'