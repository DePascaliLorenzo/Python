from contatto import Contatto
from indirizzo import Indirizzo
from repository import get_connection

def stampa_rubrica_repo():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM contatti JOIN indirizzi ON contatti.id_indirizzo = indirizzi.id'
                cursor.execute(sql)
                risultato = cursor.fetchall()
                rubrica = []
                for record in risultato:
                    indirizzo = Indirizzo(id = record[6], via = record[7], civico = record[8], cap = record[9], comune = record[10], provincia = record[11])
                    contatto = Contatto(id = record[0], nome = record[1], cognome = record[2], telefono = record[3], mail = record[4], indirizzo = indirizzo)
                    rubrica.append(contatto)
                return rubrica
    except Exception as e:
        print(e)
        return None

def aggiunta_contatto_repo(contatto, indirizzo):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                sql_indirizzo = 'INSERT INTO indirizzi (via, civico, cap, comune, provincia) VALUES (%s, %s, %s, %s, %s)'
                valori = indirizzo.via, indirizzo.civico, indirizzo.cap, indirizzo.comune, indirizzo.provincia
                cursor.execute(sql_indirizzo, valori)
                id_indirizzo = cursor.lastrowid
                sql_contatto = 'INSERT INTO contatti (nome, cognome, telefono, mail, id_indirizzo) VALUES (%s, %s, %s, %s, %s)'
                valori_contatto = contatto.nome, contatto.cognome, contatto.telefono, contatto.mail, id_indirizzo
                cursor.execute(sql_contatto, valori_contatto)
                connection.commit()
                return cursor.rowcount
    except Exception as e:
        print(e)
