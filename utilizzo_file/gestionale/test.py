from repository.prodotto_repository import *

def pannello_comandi():
    match input('***** GESTIONALE MAGAZZINO *****\n'
                'Digita 1 per stampa magazzino\n'
                'Digita 2 per aggiungere un prodotto\n'
                'Digita 3 per eliminare un prodotto\n'
                'Digita 0 per uscire   '):
        case '1':
            elenco_prodotti()



# invocazione funzione di avvio
pannello_comandi()