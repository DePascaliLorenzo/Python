from abc import ABC, abstractmethod

# definizione superclasse astratta Computer
class Computer(ABC):

    # metodo di inizializzazione
    def __init__(self, sistema_operativo):
        self.sistema_operativo = sistema_operativo

    # metodo di istanza concreto per funzionalità con logica comune a Desktop e Laptop
    def installazione_software(self, nome_software):
        print(f'Installazione di {nome_software} nel sistema operativo {self.sistema_operativo}')

    # metodo di istanza astratto per funzonalità importante ma con logica diversa tra laptop e Desktop
    @abstractmethod
    def sospensione_sistema(self):
        pass

    # override metodo di rappresentazione testuale per riscrittura completa
    def __repr__(self):
        return f'Linea Computer - Sistema Operativo: {self.sistema_operativo}'