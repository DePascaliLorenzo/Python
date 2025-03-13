from abc import ABC, abstractmethod

class Veicolo(ABC):

    def __init__(self, marca, modello, numero_targa, tariffa_giornaliera):
        self.marca = marca
        self.modello = modello
        self.numero_targa = numero_targa
        self.tariffa_giornaliera = tariffa_giornaliera
