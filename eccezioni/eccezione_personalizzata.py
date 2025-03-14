# definizione di classe di eccezione personalizzata
class MiaEccezione(Exception):

    # metodo di inizializzazione
    def __init__(self, messaggio = 'Eccezione Generica'):
        self.messaggio = messaggio

    # metodo di rappresentazione testuale
    def __str__(self):
        return self.messaggio


# acquisizione input utente
input_utente = input('Digita codice prodotto preceduto da PROD- : ')

if input_utente.startswith('PROD-'):
    print('Prodotto registrato correttamente')
else:
    try:
        raise MiaEccezione('Il codice prodotto non è corretto')
    except MiaEccezione as m:
        print(m)