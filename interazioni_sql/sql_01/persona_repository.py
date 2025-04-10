import pymysql

from interazioni_sql.sql_01.persona import Persona


# Ogni volta che l'app deve interagire con il database, deve effettuare una connessione
# Aprire una connessione richiede:
# Localizzazione del server MySQL + Credenziali + Database di riferimento
# Al termine della singola operazione, la connessione deve essere chiusa

# funzione ausiliaria per ottenere la connessione al database
def _get_connection():
    return pymysql.connect(
        host = 'localhost', # '127.0.0.1'
        port = 3306,
        user = 'root',
        password = '',
        database= 'sql_01'
    )

# funzione per registrazione di un nuovo oggetto Persona nel db
def registrazione_persona_repo(persona):
    try:
        with _get_connection() as connection:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO persone (nome, cognome, eta) VALUES (%s, %s, %s)'
                valori = persona.nome, persona.cognome, persona.eta
                cursor.execute(sql, valori)
                connection.commit()
                return cursor.rowcount
    except Exception as e:
        print(e)
        return None

# funzione per ottenere un oggetto Persona dal database (ricerca per id)
def dati_persona_repo(id):
    try:
        with _get_connection() as connection:
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM persone WHERE id=%s'
                valori = id,
                cursor.execute(sql, valori)
                risultato = cursor.fetchone() # tupla con dati record in ordine colonne e null se non trova nulla
                if risultato:
                    return Persona(risultato[0],risultato[1],risultato[2],risultato[3])
                else:
                    return 'Persona Non Trovata'
    except Exception as e:
        print(e)
        return None

# funzione per ottenere un oggetto Persona dal database (ricerca per id)
def elenco_persone_repo():
    try:
        with _get_connection() as connection:
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM persone'
                cursor.execute(sql)
                risultato = cursor.fetchall() # tupla con dati record in ordine colonne e null se non trova nulla
                if risultato:
                    return risultato
                else:
                    return 'Persona Non Trovata'
    except Exception as e:
        print(e)
        return None


# funzione per aggiornamento dati di un oggetto Persona nel db
def aggiornamento_persona_repo(persona):
    try:
        with _get_connection() as connection:
            with connection.cursor() as cursor:
                sql = 'UPDATE persone SET nome=%s, cognome=%s, eta=%s WHERE id=%s'
                valori = persona.nome, persona.cognome, persona.eta, persona.id
                cursor.execute(sql, valori)
                connection.commit()
                return cursor.rowcount
    except Exception as e:
        print(e)
        return None

# funzione per eliminazione di un oggetto Persona nel db (identificazione tramite chiave primaria)
def eliminazione_persona_repo(id):
    try:
        with _get_connection() as connection:
            with connection.cursor() as cursor:
                sql = 'DELETE FROM persone WHERE id=%s'
                valori = id
                cursor.execute(sql, valori)
                connection.commit()
                return cursor.rowcount
    except Exception as e:
        print(e)
        return None

# funzione per ottenere una lista di oggettiPersona dal database (ricerca su carattere cognome)
def elenco_persone_like_cognome_repo(sequenza_cercata):
    try:
        with _get_connection() as connection:
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM persone WHERE cognome LIKE &s'
                valori = f'%{sequenza_cercata}%', # la virgola è essenziale per rendere valori una tupla
                cursor.execute(sql)
                risultato = cursor.fetchall() # tupla con dati record in ordine colonne e null se non trova nulla
                return [Persona(id, nome, cognome, eta) for id, nome, cognome, eta in risultato]
    except Exception as e:
        print(e)
        return None
