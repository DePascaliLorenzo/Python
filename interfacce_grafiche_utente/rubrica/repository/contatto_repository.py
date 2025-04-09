import json

from interfacce_grafiche_utente.rubrica.model.contatto import Contatto


# funzione per leggere i dati dal file e ottenere una lista di oggetti Contatto
def elenco_contatti_repo():
    try:
        with open('rubrica.json') as file:
            dati_recuperati = json.load(file)
            lista_contatti = [Contatto.deserializzazione(dizionario) for dizionario in dati_recuperati]
            return lista_contatti
    except Exception as e:
        print(e)
        return None

# funzione ausiliaria per scrivere l'intera lista contatti nel file json
def _riscrittura_file(lista_contatti):
    try:
        with open('rubrica.json', 'w') as file:
            lista_contatti = [contatto.serializzazione() for contatto in lista_contatti]
            json.dump(lista_contatti, file, indent=4)
            return True
    except Exception as e:
        print(e)
        return False

# funzione per aggiungere un contatto al file json
def aggiunta_contatto_repo(contatto):
    lista_contatti = elenco_contatti_repo()
    lista_contatti.append(contatto)
    return _riscrittura_file(lista_contatti)

# funzione per eliminare un contatto dal file json
def eliminazione_contatto_repo(contatto):
    lista_contatti = elenco_contatti_repo()
    if contatto in lista_contatti:
        lista_contatti.remove(contatto)
        return _riscrittura_file(lista_contatti)