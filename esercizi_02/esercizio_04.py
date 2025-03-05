"""Simulare il comportamento progressivo di un orologio con avvio alle 0:0:0 e fine alle
23:59:59; ogni 60 secondi, deve essere azzerato il contatore dei secondi e incrementato
quello dei minuti; ogni 60 minuti, deve essere azzerato il contatore dei minuti e
incrementato quello delle ore.
OUTPUT
Stampa in console l'intera progressione come mostrato di seguito:
0:0:0
0:0:1
...
23:59:59
NOTA (per ottenere output):
Modificare impostazioni console Editor -> General -> Console -> Override console cicle
buffer 2048

"""

secondi = 0
minuti = 0
ore = 0

for ore in range(24):
    for minuti in range(60):
        for secondi in range(60):
            print(f'{ore}:{minuti}:{secondi}')