"""
Rappresentazione tabelline da 1 a 10
1  2  3  4  5  6  7  8  9  10
2  4  6  8  10 12 14 16 18 20
...
- Partire da una struttura vuota
- Popolare la struttura mediante un ciclo
- Stampa del valori della struttura in formato tabellare
"""

# Struttura vuota (lista bidimensiona -> lista di liste)
tabelline = []

# Cicli di popolamento
for indice_riga in range(10): # gestione righe (n°10 con indici da 0 a 9)
    riga = []
    for indice_cella in range(10): #gestione celle riga (n°10 con indici da 0 a 9)
        riga.insert(indice_cella, (indice_riga + 1) * (indice_cella + 1))
    tabelline.append(riga)


# Stampa tabelline
print(tabelline)

# Stampa tabelline in formato tabellare
for riga in tabelline:
    for cella in riga:
        print("{:>4}".format(cella), end=" ") # stampa cella con padding a destra di 4 spazi
    print() # a capo per nuova riga