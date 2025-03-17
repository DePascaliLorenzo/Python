from repository.prodotto_repository import *

# funzione per la stampa del magazzino
def stampa_magazzino():
    magazzino = elenco_prodotti() # [...] = prodotti recuperati - [] = nulla nel file - None = problemi in lettura
    if magazzino is not None:
        if len(magazzino) > 0:
            print('-----Magazzino-----')
            for prodotto in magazzino:
                print(prodotto)
        else:
            print('Nessun prodotto attualmente registrato')
    else:
        print('Problemi con il file di archiviazione')

# funzione per l'aggiunta di un nuovo prodotto
def aggiunta_prodotto():
    print('----- Aggiunta Prodotto -----')
    tipologia = input('Inserire tipologia: ').strip().replace(',','')
    marca = input('Inserire marca: ').strip().replace(',', '')
    modello = input('Inserire modello: ').strip().replace(',','')
    try:
        prezzo = float(input('Inserire prezzo: ').strip().replace(',','.'))
        prodotto = Prodotto(tipologia=tipologia,marca=marca,modello=modello,prezzo=prezzo)
        print(registrazione_prodotto(prodotto))
    except ValueError as v:
        print('Il prezzo che hai inserito non è valido')
        pannello_comandi()

# funzione per la cancellazione di un prodotto
def cancellazione_prodotto():
    magazzino = elenco_prodotti()
    if magazzino is None:
        print('Problemi con il file di archiviazione')
    elif len(magazzino) == 0:
        print('Nessun prodotto attualmente registrato')
    else:
        print('----- Cancellazione Prodotto -----')
        for prodotto in magazzino:
            print(prodotto)
        try:
            id_prodotto = int(input('Inserire l\'id del prodotto da eliminare: ').strip())
            prodotto_da_eliminare = list(filter(lambda p: p.id == id_prodotto, magazzino))[0]
            magazzino.remove(prodotto_da_eliminare)
            print(eliminazione_prodotto(magazzino))
        except Exception as e:
            print('Input errato o Prodotto non trovato')
            pannello_comandi()


# funzione di avvio e gestione applicazione
def pannello_comandi():
    match input('***** GESTIONALE MAGAZZINO *****\n'
                'Digita 1 per stampa magazzino\n'
                'Digita 2 per aggiungere un prodotto\n'
                'Digita 3 per eliminare un prodotto\n'
                'Digita 0 per uscire   '):
        case '1':
            stampa_magazzino()
            pannello_comandi()
        case '2':
            aggiunta_prodotto()
            pannello_comandi()
        case '3':
            cancellazione_prodotto()
            pannello_comandi()
        case _:
            exit(0)


# invocazione funzione di avvio
pannello_comandi()