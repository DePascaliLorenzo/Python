import csv
from esercizi_05.model.fattura import Fattura

_FILE_PATH = 'REGISTRI/emesse.csv'

def elenco_fatture():
    try:
        with open(_FILE_PATH) as file:
            contenuto = csv.reader(file)
            next(contenuto)
            fatture = []
            for riga in contenuto:
                fattura = Fattura(int(riga[0]),riga[1],riga[2],riga[3],riga[4],float(riga[5]),int(riga[6]))
                fatture.append(fattura)
            return fatture
    except Exception as e:
        print(e)
        return None

def _generatore_id():
    fatture = elenco_fatture()
    if fatture is None:
        return None
    if len(fatture) == 0:
        return 0
    return max(list(map(lambda fattura: fattura.id, fatture))) + 1

def registrazione_fattura(fattura):
    id_nuova_fattura= _generatore_id()
    if id_nuova_fattura is None:
        return 'Problemi con il file di archiviazione'
    try:
        with open(_FILE_PATH, 'a', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow([id_nuova_fattura, fattura.data_emissione.strftime('%d-%m-%Y'),fattura.descrizione,fattura.nome_cliente,fattura.cognome_cliente,fattura.importo,fattura.iva,fattura.totale])
            return 'Fattura registrata correttamente'
    except Exception as e:
        print(e)
        return 'Registrazione impossibile'