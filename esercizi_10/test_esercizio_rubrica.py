"""
Esercitazione Rubrica
Crea un progetto chiamato “esercitazione-rubrica”

ESERCIZIO

Realizzare, secondo il paradigma Object Oriented, un’applicazione Rubrica per la gestione dei contatti; l’applicativo,
in collaborazione con un database MySql fornito in allegato, dovrà permettere di:
I. Registrare, acquisendo i dati mediante console, un contatto con relativo indirizzo
II. Stampare in console l’intero elenco contatti con indicazione di tutti i dati disponibili (compreso l’indirizzo)

Si raccomanda, per quanto possibile, di evitare la generazione di potenziali eccezioni in rapporto allo schema del database fornito.
"""
from rubrica_repository import *

def test_aggiunta_rubrica():
    nome = input('Digita il NOME del nuovo contatto: ')
    cognome = input('Digita il COGNOME del nuovo contatto: ')
    telefono = input('Digita il NUMERO DI TELEFONO del nuovo contatto: ')
    mail = input('Digita l\'INDIRIZZO E-MAIL del nuovo contatto: ')
    via = input('Digita la VIA del nuovo contatto: ')
    civico = input('Digita il NUMERO CIVICO del nuovo contatto: ')
    cap = input('Digita il CAP del nuovo contatto: ')
    comune = input('Digita il COMUNE DI RESIDENZA del nuovo contatto: ')
    provincia = input('Digita la PROVINCIA del nuovo contatto: ')
    contatto = Contatto(nome,cognome,telefono, mail)
    indirizzo = Indirizzo(via, civico, cap, comune, provincia)
    print(aggiunta_contatto_repo(contatto, indirizzo))

def stampa_rubrica():
    rubrica = stampa_rubrica_repo()
    if rubrica is None:
        print('Errore di comunicazione con il database')
    else:
        if len(rubrica) == 0:
            print('Rubrica vuota')
        else:
            for contatto in rubrica:
                print(contatto)

print('***** MENU\' *****')
selezione = input('Digita 1 per aggiungere un contatto, 2 per stampare la rubrica: ')
match selezione:
    case '1':
        test_aggiunta_rubrica()
    case '2':
        stampa_rubrica()
    case _:
        print('Opzione non valida')