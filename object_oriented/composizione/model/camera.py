# definizione classe di modellazione oggetto Camera
class Camera:

    # metodo di inizializzazione
    def __init__(self, numero, tipologia, tariffa_notte):
        self.numero = numero
        self.tipologia = tipologia
        self.tariffa_notte = tariffa_notte

    # metodo di istanza per rappresentazione testuale
    def __repr__(self):
        return f'Camera n°{self.numero} - {self.tipologia} - Tariffa: {self.tariffa_notte}'
