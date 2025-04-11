import threading


class Negozio:

    def __init__(self):
        self.occupato = False
        self.condition = threading.Condition()

    # metodo per la gestione dell'ingresso nel negozio (risorsa)
    def ingresso(self, cliente):
        with self.condition:
            while self.occupato:
                self.condition.wait()
        self.occupato = True
        print(f'{cliente} entra nel negozio')

    # metodo per la gestione per l'uscita dal negozio (risorsa)
    def uscita(self, cliente):
        with self.condition:
            self.occupato = False
            print(f'{cliente} esce dal negozio')
            self.condition.notify_all()
