"""
Sviluppa un'applicazione secondo i seguenti criteri:
• Richiedi in input il nome di giocatore1
• Richiedi in input il nome di giocatore2
• Richiedi in input a giocatore1 la sua scelta (no validazione) tra:
◦ S - sasso
◦ C - carta ◦ F - forbici
• Richiedi in input a giocatore2 la sua scelta (no validazione) tra:
◦ S - sasso
◦ C - carta ◦ F - forbici
• Effettua gli opportuni controlli per determinare il risultato:
◦ sasso batte forbici
◦ carta batte sasso
◦ forbici battono carta
◦ parità
• Ritorna in output il nome del vincitore oppure un messaggio indicante la parità
"""

giocatore1 = input("Inserisci il nome del primo giocatore: ")
giocatore2 = input("Inserisci il nome del secondo giocatore: ")

scelta_g1 = input("Scegli tra S - sasso, C - carta, F - forbici: ")
scelta_g2 = input("Scegli tra S - sasso, C - carta, F - forbici: ")

if scelta_g1 == scelta_g2:
    print('parità')
elif scelta_g1 == "S" and scelta_g2 == "C":
    print('Il vincitore è', giocatore2)
elif scelta_g1 == "S" and scelta_g2 == "F":
    print('Il vincitore è', giocatore1)
elif scelta_g1 == "C" and scelta_g2 == "S":
    print('Il vincitore è', giocatore1)
elif scelta_g1 == "C" and scelta_g2 == "F":
    print('Il vincitore è', giocatore2)
elif scelta_g1 == "F" and scelta_g2 == "S":
    print('Il vincitore è', giocatore2)
elif scelta_g1 == "F" and scelta_g2 == "C":
    print('Il vincitore è', giocatore1)
else:
    print('Qualcosa è andato storto')