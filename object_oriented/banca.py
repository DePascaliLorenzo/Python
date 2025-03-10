"""
SIMULAZIONE SOFTWARE BANCA
- Possibilità di aprire un conto corrente ricevendo IBAN (saldo 0)
- Possibilità di registrare versamenti e prelevamenti (quanti ne vuole)
- Possibilità di terminare il programma in qualsiasi momento

SVILUPPO OBJECT ORIENTED -> Oggetto lofico da gestire è ContoCorrente
                            . Intestatario (nome e cognome del cliente)
                            . Saldo
                            . Numero conto (casuale)
                            . IBAN (parte fissa + numero del conto)
                            . Costruzione oggetto ContoCorrente ad apertura
                            . Aggiornamento dinamico saldo conto corrente
                            . Rappresentazione testuale dell'oggetti
"""
import random

# definizione classe di modellazione ogetto ContoCorrente
class ContoCorrente:

    # attributo di classe con valore comune a tutti gli oggetti
    iban_fisso = 'IT 07 K 02008 13000'

    # metodo di inizializzazione
    def __init__(self, intestatario):
        self.intestatario = intestatario
        self.saldo = 0
        self.numero_conto = "".join(str(random.randint(0,9)) for _ in range(7))
        self.iban = ContoCorrente.iban_fisso + self.numero_conto

    # metodo di istanza di aggiornamento saldo (invocato ad ogni operazione)
    def set_saldo(self, importo_operazione): # se 100.78 ok... se ciao no
        try:
            importo_operazione = float(importo_operazione.strip().replace(',','.'))
            self.saldo += importo_operazione
            return f"Hai registrato un'operazione di {importo_operazione:.2f} ed ora hai un saldo pari a {self.saldo}"
        except Exception as e:
            return "L'importo che hai inserito non è corretto"


    # metodo di istanza per rappresentazione testuale
    def __repr__(self):
        return f"Benvenuto/a {self.intestatario}\nL'IBAN del tuo nuovo conto è {self.iban}\nAttualmente il tuo saldo è pari a {self.saldo} €"

def pannello_comandi():
    scelta_utente = input(
        "***** La Tua Banca *****\n"
        "Digita 1 per aprire il tuo conto\n"
        "Digita 0 per terminare\n")
    match scelta_utente:
        case '1':
            apertura_conto()
        case _:
            print("Arrivederci... Alla prossima.")
            exit(1)

def apertura_conto():
    nome_cognome = input("Grazie di aver scelto di aprire un conto!\nInserisca nome e cognome: ")
    conto = ContoCorrente(nome_cognome)
    print(conto)
    scelta_utente = input('Desideri effettuare delle operazioni? (SI o NO) ')
    if scelta_utente.upper() == "SI":
        registrazione_operazione(conto)
    else:
        print(f'Arrivederci {conto.intestatario}... Alla prossima')

# funzione per gestire registrazione operazioni
def registrazione_operazione(conto):
    while True:
        importo = input('Digita importo operazione (oppure 0 per terminare): ')
        if importo != "0":
            print(conto.set_saldo(importo))
        else:
            print(f"Arrivederci {conto.intestatario}... Alla prossima")
            exit(2)

pannello_comandi()
