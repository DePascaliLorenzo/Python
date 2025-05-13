import pymysql

try:
    conn = pymysql.connect(
        host="localhost",    # Indirizzo del server MySQL
        port = 3306,
        user="root",   # Nome utente MySQL
        password="",  # Password MySQL
        database="residenti"  # Nome del database
    )

    if conn:
        print("Connessione al database 'residenti' riuscita!")

        # Creazione di un cursore per eseguire query
        cursor = conn.cursor()

        # Esecuzione di una query di test
        sql = "SELECT * FROM popolazione"
        cursor.execute(sql)
        result = cursor.fetchone()
        print("Database attivo:", result[0])

        # Chiudi il cursore e la connessione
        conn.commit()
        cursor.rowcount()
        print("Connessione chiusa.")

except pymysql.connect.Error as err:
    print(f"Errore di connessione: {err}")