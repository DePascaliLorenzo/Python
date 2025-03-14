from esercizi_04.model.autovettura import Autovettura
from esercizi_04.model.cliente import Cliente
from esercizi_04.model.furgone import Furgone
from esercizi_04.model.noleggio import Noleggio

#GRUPPO 2 ANA MARIA, GUIDO, LUCA, FRA

veicoli = []
clienti = []
noleggi = []

def registra_autovettura(marca, modello, numero_targa, tariffa_giornaliera, numero_porte, tipologia_cambio):
    veicoli.append(Autovettura(marca, modello, numero_targa, tariffa_giornaliera, numero_porte, tipologia_cambio))
    return Autovettura(marca, modello, numero_targa, tariffa_giornaliera, numero_porte, tipologia_cambio)

def registra_furgone(marca, modello, numero_targa, tariffa_giornaliera, portata, dimensioni):
    veicoli.append(Furgone(marca, modello, numero_targa, tariffa_giornaliera, portata, dimensioni))
    return Furgone(marca,modello,numero_targa, tariffa_giornaliera, portata, dimensioni)

def registra_cliente(nome, cognome, numero_patente):
    clienti.append(Cliente(nome,cognome,numero_patente))
    return Cliente(nome,cognome,numero_patente)

def registra_noleggio():

    scelta = input('\nDigita A per registrare una auto.\nDigita F per registrare un furgone.\nDigita C per registrare un cliente.\nDigita N per effettuare un noleggio.\nDigita L per visualizzare le liste.\n')
    match scelta:
        case "A" | "a":
            marca = input("Inserisci la marca dell'auto: ")
            modello = input("Inserisci il modello dell'auto: ")
            numero_targa = input("Inserisci il numero di targa: ")
            tariffa_giornaliera = int(input("Inserisce la tariffa giornaliera: "))
            numero_porte = input("Inserisci il numero di porte: ")
            tipologia_cambio = input("Inserisci il tipo di cambio: ")
            registra_autovettura(marca, modello, numero_targa, tariffa_giornaliera, numero_porte, tipologia_cambio)
        case "F" | "f":
            marca = input("Inserisci la marca del furgone: ")
            modello = input("Inserisci il modello del furgone: ")
            numero_targa = input("Inserisci il numero di targa: ")
            tariffa_giornaliera = int(input("Inserisce la tariffa giornaliera: "))
            portata = input("Inserisci la portata in KG: ")
            dimensioni = input("Inserisci le dimensioni in cm: ")
            registra_furgone(marca, modello, numero_targa, tariffa_giornaliera, portata, dimensioni)
        case "C" | "c":
            nome = input("Inserisci il nome del cliente: ")
            cognome = input("Inserisci il cognome del cliente: ")
            numero_patente = input("Inserisci il numero della patente del cliente: ")
            registra_cliente(nome,cognome,numero_patente)
        case "N" | "n":
            data_inizio = input("Inserisci data di inizio del noleggio in formato gg-mm-aaaa: ")
            data_fine = input("Inserisci data di fine del noleggio in formato gg-mm-aaaa: ")
            nuovo_noleggio = Noleggio(data_inizio,data_fine,clienti[0],veicoli[0])
            noleggi.append(nuovo_noleggio)
        case "L" | "l":
            print(veicoli)
            print('')
            print(clienti)
            print('')
            print(noleggi)
        case _:
            print('errore')
            exit(0)

while True:
    registra_noleggio()