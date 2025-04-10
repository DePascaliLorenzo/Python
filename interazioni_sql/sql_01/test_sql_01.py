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

# funzione per testare la stampa dell'elenco persone
def test_elenco_persone():
    esito = elenco_persone_repo()
    if esito is None:
        print('Errore di comunicazione con il database')
    else:
        if len(esito) == 0:
            print('Nessuna persona registrata')
        else:
            for persona in esito:
                print(persona)

# funzione per testare l'aggiornamento
def test_aggiornamento():
    test_elenco_persone()
    id_persona_da_modificare = int(input('Digita id della persona da modificare: '))
    persona = dati_persona_repo(id_persona_da_modificare) # Persona oppure str oppure None
    persona.nome = input(f'Modifica il Nome della persona (Nome originario: {persona.nome}): ')
    persona.cognome = input(f'Modifica il Cognome della persona (Cognome originario: {persona.cognome}): ')
    persona.eta = int(input(f'Modifica l\'età della persona (Età originaria: {persona.eta}): '))
    print(aggiornamento_persona_repo(persona))

# funzione per testare l'eliminazione
def test_eliminazione():
    id_persona_da_eliminare = int(input('Digita id della persona da eliminare: '))
    print(eliminazione_persona_repo(id_persona_da_eliminare))

# funzione per testare la ricerca
def test_ricerca():
    sequenza_caratteri = input('Digita i caratteri da cercare: ')
    esito = elenco_persone_like_cognome_repo(sequenza_caratteri)
    if esito is not None:
        for persona in esito:
            print(persona)

# invocazione funzioni
# test_registrazione()
# test_dati_persona()
# test_elenco_persone()
# test_aggiornamento()
# test_eliminazione()
test_ricerca()