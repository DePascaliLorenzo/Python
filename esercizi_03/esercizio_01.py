"""
In uno script denominato esercizio_01, realizzare una classe chiamata Cerchio.
Tale classe dovrà avere una struttura tale da permettere, ad ogni oggetto istanziato,
di calcolare e rappresentare la sua area e la sua circonferenza.
Utilizzare le funzionalità della classe nell'ambito del medesimo script per testare la struttura realizzata.
"""
class Cerchio:

    cerchi = []

    pigreco = 3.14

    def __init__(self, raggio):
        self.raggio = raggio
        self.circonferenza = raggio * Cerchio.pigreco
        self.area = Cerchio.pigreco * raggio**2

    def __repr__(self):
        return f'Il tuo cerchio ha un raggio di {self.raggio} cm.\nLa sua circonferenza è uguale a: {self.circonferenza} cm\nLa sua area è uguale a: {self.area} cm2\n'

    @classmethod
    def popolamento_cerchi(cls, *args):
        for cerchio in args:
            cls.cerchi.append(cerchio)

while True:
    raggio = float(input("Inserisci il raggio del nuovo cerchio, oppure 0 per uscire: "))
    if raggio == 0:
        print('Chiusura programma')
        exit(1)
    else:
        cerchio = Cerchio(raggio)
        Cerchio.popolamento_cerchi(cerchio)
        print(Cerchio.cerchi)