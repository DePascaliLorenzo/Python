# liste per ospitare i dati
nomi = []
cognomi = []

# acquisizione input utente x 2 contatti
for _ in range(2):
    nome = input('Inserire nome contatto: ')
    cognome = input('Inserire cognome contatto: ')
    nomi.append(nome)
    cognomi.append(cognome)

# lettura dati registrati
for indice in range(0, len(nomi)):
    print('CONTATTO')
    print('Nome: ', nomi[indice])
    print('Cognome: ', cognomi[indice])
    print('--------------------------')