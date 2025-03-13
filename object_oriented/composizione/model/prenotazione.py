from datetime import datetime

# definizione classe di modellazione oggetto Prenotazione
# mediante pattern di composizione -> Prenotazione ha un Cliente e ha una Camera
class Prenotazione:

    # metodod di inizializzazione
    def __init__(self, data_arrivo, data_partenza, cliente, camera):
        self.data_arrivo = datetime.strptime(data_arrivo, '%d-%m-%Y').date()
        self.data_partenza = datetime.strptime(data_partenza, '%d-%m-%Y').date()
        self.cliente = cliente
        self.camera = camera
        self.importo = self.calcolo_importo()

    # metodo di istanza per logica di calcolo importo
    def calcolo_importo(self):
        differenza_notti = (self.data_partenza - self.data_arrivo).days
        importo = differenza_notti * self.camera.tariffa_notte
        return round(importo, 2)

    # metodo di istanza per rappresentazione testuale
    def __repr__(self):
        return (f'Prenotazione dal: {self.data_arrivo.strftime('%d-%m-%Y')} al: {self.data_partenza.strftime('%d-%m-%Y')}'
                f'\n{self.camera}\n{self.cliente}\nTotale soggiorno: {self.importo} €')
