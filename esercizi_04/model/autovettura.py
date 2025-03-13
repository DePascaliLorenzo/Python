from esercizi_04.model.veicolo import Veicolo

class Autovettura(Veicolo):

    def __init__(self,marca, modello, numero_targa, tariffa_giornaliera, numero_porte, tipologia_cambio):
        super().__init__(marca, modello, numero_targa, tariffa_giornaliera)
        self.numero_porte = numero_porte
        self.tipologia_cambio = tipologia_cambio
