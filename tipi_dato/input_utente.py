# acquisizione input utente e stoccaggio in variabili
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
eta = input("Inserisci la tua età: ")

# qualsiasi input ritornerà sempre una stringa

# analisi dei dati ricevuti
print(nome, type (nome))
print(cognome, type (cognome))
print(eta, type (eta))

# conversione input in valore numerico
eta = int(eta)
print(eta, type (eta))

# output utente
print(f"Ti chiami {nome} {cognome} e hai {eta} anni")