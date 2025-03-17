# funzione per scrivere testo su un file che verrà creato
def scrivi_su_file(testo):
    file = None
    try:
        file = open('file.txt', 'w') # apertura stream in modalità scrittura / sovrascrittura
        file.write(testo)
    except Exception as e:
        print(e)
    finally:
        if file:
            file.close()

# funzione per aggiungerà testo su un file che, se non esiste, verrà creato
def aggiungi_a_file(testo):
    file = None
    try:
        file = open('file2.txt', 'a') # apertura stream in modalità append (o aggiunta)
        file.write(testo)
    except Exception as e:
        print(e)
    finally:
        if file:
            file.close()

# funzione per scrivere testo su un file con gestione automatica della chiusura
def scrivi_e_chiudi(testo):
    try:
        with open('file3.txt', 'x') as file: # apertura stream in modalità protetta
            file.write(testo)
    except Exception as e:
        print(e)

# invocazione funzioni
scrivi_su_file('Prima linea del file')
aggiungi_a_file('Prima riga di testo')
scrivi_e_chiudi('Prima riga di testo')