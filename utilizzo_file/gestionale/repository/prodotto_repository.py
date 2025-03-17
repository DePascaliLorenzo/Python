import csv
from utilizzo_file.gestionale.model.prodotto import Prodotto

# costante per riferimento al file di archiviazione
_FILE_PATH = 'magazzino.csv'

# funzione per leggere il contenuto del file ottenendo una lista di oggetti Prodotto
def elenco_prodotti():
    try:
        with open(_FILE_PATH) as file:
            contenuto = csv.reader(file) # ritorna una struttura iterabile
            next(contenuto)
            prodotti = []
            for riga in contenuto:
                prodotto = Prodotto()
                prodotto.id = int(riga[0])
                prodotto.tipologia = riga[1]
                prodotto.marca = riga[2]
                prodotto.modello = riga[3]
                prodotto.prezzo = float(riga[4])
                prodotti.append(prodotto)
            return prodotti
    except Exception as e:
        print(e)
        return None


# funzione ausiliaria per generare id progressivo in fase di registrazione
def _generatore_id():
    prodotti = elenco_prodotti()
    if prodotti is None:
        return None
    if len(prodotti) == 0:
        return 0
    return max(list(map(lambda prodotto: prodotto.id, prodotti))) + 1

def registrazione_prodotto(prodotto):
    id_nuovo_prodotto = _generatore_id()
    if id_nuovo_prodotto is None:
        return 'Problemi con il file di archiviazione'
    try:
        with open(_FILE_PATH, 'a', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow([id_nuovo_prodotto, prodotto.tipologia, prodotto.marca, prodotto.modello, prodotto.prezzo])
            return 'Prodotto registrato correttamente'
    except Exception as e:
        print(e)
        return 'Registrazione impossibile'

# funzione per eliminare un prodotto dal file
def eliminazione_prodotto(magazzino):
    try:
        with open(_FILE_PATH, 'w', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(['Id','Tipologia','Marca','Modello','Prezzo'])
            writer.writerows([prodotto.to_list() for prodotto in magazzino])
            return 'Prodotto Eliminato'
    except Exception as e:
        print(e)
        return 'Eliminazione impossibile'