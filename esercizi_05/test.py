# gruppo 3: Francesca Muollo - Giovanni Nardella - Mario Girolamo
from esercizi_05.REGISTRI.emesse_repository import elenco_fatture, registrazione_fattura
from esercizi_05.model.fattura import Fattura


def aggiunta_fattura():
    print('\n***** REGISTRAZIONE FATTURA *****')
    data_emissione = input('Inserire la data di emissione della fattura in formato gg-mm-aaaa: ')
    descrizione = input('Inserire una breve descrizione: ')
    nome_cliente = input('Inserire il nome del cliente: ')
    cognome_cliente = input('Inserire il cognome del cliente: ')
    importo = 0.0
    try:
        importo = float(input('Inserire l\'importo della fattura: ').replace(',','.'))
    except ValueError as v:
        print('L\'importo inserito non è valido. Riprova.')
        pannello_comandi()
    try:
        iva = int(input('Inserire l\'IVA: '))
        print(iva)
        fattura = Fattura(data_emissione=data_emissione,descrizione=descrizione,nome_cliente=nome_cliente,cognome_cliente=cognome_cliente,importo=importo,iva=iva)
        print(fattura)
        print(registrazione_fattura(fattura))
    except ValueError as v:
        print('L\'IVA inserita non è valida. Riprova.')
        pannello_comandi()

def visualizza_fatture():
    fatture = elenco_fatture()
    print(fatture)

def visualizza_totale():
    fatture = elenco_fatture()
    totale = 0.0
    for riga in fatture:
        totale += riga.totale
    print(f'Il totale delle fatture emesse è: {totale:.2f} €')

def pannello_comandi():
    match input('\n***** GESTIONALE FATTURE *****\n'
                'Digita 1 per registrare una fattura\n'
                'Digita 2 per visualizzare tutte le fatture\n'
                'Digita 3 per visualizzare tutte le fatture E il totale imponibile delle fatture\n'
                'Digita 0 per uscire   '):
        case '1':
            aggiunta_fattura()
            pannello_comandi()
        case '2':
            visualizza_fatture()
            pannello_comandi()
        case '3':
            visualizza_fatture()
            visualizza_totale()
            pannello_comandi()
        case _:
            exit(0)

# invocazione funzione di avvio
pannello_comandi()