from abc import ABC, abstractmethod

# definizione superclasse astratta Dispositivo (collegamento tra le 2 linee di produzione)
class Dispositivo(ABC):

    # metodo di istanza concreto per una funzionalità non utilizzata da tutti con logica comune per chi la utilizza
    def ricarica_batteria(self):
        print('Batteria scarica... collega alla presa di corrente')

    # metodo di istanza asyratto per funzionalità importante per tutti ma logiche diverse tra tutti
    @abstractmethod
    def inizializzazione_dispositivo(self):
        pass