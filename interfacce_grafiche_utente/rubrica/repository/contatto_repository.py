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