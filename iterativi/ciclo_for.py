# Dobbiamo stampare 10 volte la frase "Ciao mondo!" tenendo il conteggio delle iterazioni.

for contatore in range(10):
    print(f"Ciao mondo! {contatore}") # stampa la stringa 10 volte

print('\n')

# Dobbiamo stampare 10 volte la frase "Ciao mondo!" tenendo il conteggio delle iterazioni (1-10).
for contatore in range(1,11):
    print(f"Ciao mondo! -> a questo giro il contatore vale {contatore}") # stampa la stringa 10 volte

print ('\n')

# Iteriamo gli elementi di una lista per stamparli
lista = ['uno', 'due', 'tre', 'quattro']
for elemento in lista:
    print(elemento)