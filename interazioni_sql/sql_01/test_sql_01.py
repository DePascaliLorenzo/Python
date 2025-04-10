from persona_repository import *
from persona import Persona

# funzione per testare la registrazione
def test_registrazione():
    nome = input('Digita nome: ')
    cognome = input('Digita cognome: ')
    eta = int(input('Digita età: '))
    persona = Persona(nome = nome, cognome = cognome, eta = eta)
    print(registrazione_persona_repo(persona))

# funzione per testare ottenimento dati singoli
def test_dati_persona():
    id_persona = int(input('Digita id della persona da cercare: '))
    esito = dati_persona_repo(id_persona)
    if esito:
        print(esito)
    else:
        print('Errore di comunicazione con il database')

def test_elenco_persone():
    esito = elenco_persone_repo()
    if esito:
        print(esito)
    else:
        print('Errore di comunicazione con il database')


# invocazione funzioni
# test_registrazione()
# test_dati_persona()
# test_elenco_persone()