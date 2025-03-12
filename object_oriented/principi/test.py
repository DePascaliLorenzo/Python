from model.studente import Studente
from model.lavoratore import Lavoratore

# dichiarazione e istanziazione oggetti da gestire
studente = Studente('Mario','Rossi',20, 8.5)
lavoratore = Lavoratore('Gianni', 'Verdi', 55, 1300.55)
print(studente)
print(lavoratore)

# invocazione metodi e attributi
print(studente.eta)
print(lavoratore.cognome)
print(studente.media_voti)
print(lavoratore.reddito)
studente.camminare()
studente.fare_qualcosa()
lavoratore.camminare()
lavoratore.fare_qualcosa()
studente.annotazione_appunti()
lavoratore.richiesta_permesso()