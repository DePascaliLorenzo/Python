import pymysql

# funzione invocabile al bisogno per ottenere la connessione al database
def get_connection():
    return pymysql.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '',
        database = 'esercizio_rubrica_base'
    )