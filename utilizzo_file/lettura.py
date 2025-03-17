# funzione per leggere il contenuto di un file
def leggi_file():
    try:
        with open('file2.txt','r') as file:
            contenuto = file.read()
            print(contenuto, type(contenuto))
    except Exception as e:
        print(e)

# funzione per leggere il contenuto di un file e ritornarlo sotto forma di lista di stringhe contenenti le varie righe
def leggi_linee_file():
    try:
        with open('file2.txt') as file:
            contenuto = file.readlines()
            print(contenuto, type(contenuto))
    except Exception as e:
        print(e)

#invocazione funzioni
leggi_file()
leggi_linee_file()