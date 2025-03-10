# classe di modellazione oggetti di tipo Contatto
class Contatto:

    # attributo di classe per collezionamento contatti
    contatti = []

    # metodo di inizializzazione
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        Contatto.contatti.append(self)

    # metodo di rappresentazione testuale
    def __repr__(self):
        return f"CONTATTO\nNome: {self.nome}\nCognome: {self.cognome}\n------------------------"

# acquisizione input utente
for _ in range(2):
    n = input('Inserire nome contatto: ')
    c = input('Inserire cognome contatto: ')
    Contatto(n, c)

# lettura dati registrati
for contatto in Contatto.contatti:
    print(contatto)