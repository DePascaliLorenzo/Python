import csv

# costante per riferimento al file di archiviazione
_FILE_PATH = 'magazzino.csv'

# funzione per leggere il contenuto del file ottenendo una lista di oggetti Prodotto
def elenco_prodotti():
    try:
        with open(_FILE_PATH) as file:
            contenuto = csv.reader(file) # ritorna una struttura iterabile
            for riga in contenuto:
                print(riga, type(riga))
    except Exception as e:
        print(e)