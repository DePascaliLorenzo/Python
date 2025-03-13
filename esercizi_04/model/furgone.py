from esercizi_04.model.veicolo import Veicolo

class Furgone(Veicolo):

    def __init__(self, marca, modello, numero_targa, tariffa_giornaliera, portata, dimensioni):
        super().__init__(marca, modello, numero_targa, tariffa_giornaliera)
        self.portata = portata
        self.dimensioni = dimensioni