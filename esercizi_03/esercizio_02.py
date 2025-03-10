"""
In uno script denominato esercizio_02, realizzare una classe chiamata Orologio.
Ogni oggetto istanziato da tale classe dovrà:
I. Rappresentarsi nel seguente formato progressivo 0:0:0 ... 23:59:59
II. Godere di una funzionalità di avvio
Utilizzare le funzionalità della classe nell'ambito del medesimo script per testare la struttura realizzata.
"""
from time import sleep
class Orologio:

    def __init__(self, acceso):
        self.acceso = acceso
        self.ora = 0
        self.minuto = 0
        self.secondo = 0

    def __repr__(self):
        return f'{self.ora}:{self.minuto}:{self.secondo}'

    def avvio(self):
        for self.ora in range(24):
            for self.minuto in range(60):
                for self.secondo in range(60):
                    print(self)
                    sleep(1)

orologio_uno = Orologio(False)
print(orologio_uno)
accensione = input("Vuoi accendere l'orologio? (SI/NO) ")
if accensione.upper() != "SI":
    print('Orologio lasciato spento')
    exit(2)
else:
    orologio_uno.acceso = True
    orologio_uno.avvio()