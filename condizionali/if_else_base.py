# acquisizione input utente (genere)
genere = input("Digita F per femmina o M per maschio: ")

# output utente in base a valutazione input
if genere.upper() == 'F': # upper() trasforma la stringa in maiuscolo
    print("Benvenuta")
elif genere.upper() == 'M':
    print("Benvenuto")
elif not genere: #caso senza input
    print('Non hai digitato niente')
else:
    print("Hai digitato qualcosa che non capisco")