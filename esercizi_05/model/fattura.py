from datetime import datetime

class Fattura:

    def __init__(self,id = None, data_emissione = None, descrizione = None, nome_cliente = None, cognome_cliente = None, importo = None, iva = None):
        self.id = id
        self.data_emissione = datetime.strptime(data_emissione, '%d-%m-%Y').date()
        self.descrizione = descrizione
        self.nome_cliente = nome_cliente
        self.cognome_cliente = cognome_cliente
        self.importo = importo
        self.iva = iva
        self.totale = importo + (importo * iva / 100)
        self.totale.__round__(2)

    def __repr__(self):
        return (f'N° Fattura: {self.id} - Data Emissione: {self.data_emissione.strftime('%d-%m-%Y')}\nDescrizione: {self.descrizione}\nNome e Cognome Cliente: {self.nome_cliente} {self.cognome_cliente}'
                f'\nImporto senza IVA: {self.importo:.2f} € - IVA: {self.iva}%\nTotale Fattura: {self.totale:.2f} €\n')

    def to_list(self):
        return[self.id,self.data_emissione,self.descrizione,self.nome_cliente,self.cognome_cliente,self.importo,self.iva,self.totale]
