# dichiarazione e istanziazione di variabili per stringhe
stringa_uno = "Ciao Mondo" # literal
print(stringa_uno, type(stringa_uno))
stringa_due = str("Ciao Mondo") # con costruttore di classe str
print(stringa_due, type(stringa_due))
stringa_tre = str(156.10)
print(stringa_tre, type(stringa_tre))
stringa_quattro = 'ciao' # apici singoli e doppi non cambia nulla
stringa_cinque = """
Sono una stringa
    su più linee
 e supporto l'indentazione
"""
print(stringa_cinque)

# stringa formattata
numero = 20
# stringa_sei = "Il valore della variabile numero è " + numero commentato perché da errore
stringa_sei = f"Il valore della variabile numero è {numero}"
print(stringa_sei)

# stringa con valutazione di espressioni matematiche
print(eval("15 * (4-2) ** 2 + 1"))

#operatori utilizzati sulle stringhe
stringa_sette = 'Ciao'
stringa_otto = 'Mondo'
print(stringa_sette + stringa_otto)
print(stringa_sette * 3)

# alcuni metodi e funzioni utilizzabili sulle stringhe

print(len(stringa_uno)) # ritorna lunghezza stringa (n° caratteri che la compongono)
print(stringa_uno.find('i')) # ritorna idice 1^occorrenza (indici in base 0)
print(f"L'indice della prima i nella stringa è {stringa_uno.find('i')}")
stringa_uno.replace('o','*')
print(stringa_uno)
stringa_uno = stringa_uno.replace('o','*')
print(stringa_uno)

#slicing su stringhe

stringa_lunga = 'supercalifragilistichespiralitoso'
print(stringa_lunga[2:9]) # stampa una parte della stringa, in questo caso dall'indice 2 al 9
print(stringa_lunga[3:]) # stampa una parte della stringa, in questo caso dall'indice 3 fino alla fine
print(stringa_lunga[:10]) # stampa una parte della stringa, in questo caso dall'inizio fino all'indice 10
print(stringa_lunga[3]) # stampa il carattere della stringa, in questo caso il carattere a indice 3
print(stringa_lunga[-4:]) # stampa gli ultimi caratteri della stringa fino alla fine, in questo caso gli ultimi 4
print(stringa_lunga[::2]) # stampa da inizio a fine naturale della stringa con passo a 2
print(stringa_lunga[::-1]) # stampa all'indietro a passo 1

#operatore di identità is per stringhe

stringa_nove = "a" * 20000
stringa_dieci = "a" * 20000
print(stringa_nove == stringa_dieci)
print(stringa_nove is stringa_dieci)