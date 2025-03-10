"""
Realizzare, in stile Object Oriented, un'applicazione che consenta, mediante input console,
la registrazione di un singolo utente e rispetti i seguenti requisiti:
I. L'Utente sarà rappresentato da:
• nome (richiesto in input)
• cognome (richiesto in input) • età (richiesta in input)
• password (da generare automaticamente)
II. In fase di registrazione, deve essere generata automaticamente una password composta,
se possibile, dalle ultime 3 lettere del nome e dalle prime 3 lettere del cognome;
se non possibile, dovrà essere generata una password con una sequenza di 6 caratteri casuali.
III. L'applicazione deve poter gestire tutte le possibili eccezioni dovute ad input
erronei, mancanti o che non soddisfino i requisiti richiesti.
"""
import random

class Utenza:

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        if len(nome)>2 or len(cognome)>2:
            self.password = nome[-3:] + cognome[:3]
        else:
            self.password = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))

    def __repr__(self):
        return f'Nome Utente: {self.nome}\nCognome Utente: {self.cognome}\nPassword: {self.password}'

while True:
    nome_utente = input('Inserisci nuovo nome utente (oppure 0 per uscire): ')
    if nome_utente == '0':
        print('Sei uscito dal programma')
        exit(5)
    else:
        cognome_utente = input('Inserisci nuovo cognome utente: ')
        nuova_utenza = Utenza(nome_utente, cognome_utente)
        print(nuova_utenza)