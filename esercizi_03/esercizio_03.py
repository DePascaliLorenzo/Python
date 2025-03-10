"""
In uno script denominato esercizio_03, realizzare una classe chiamata Telecomando.
Ogni oggetto, istanza di questa classe, dovrà essere rappresentato da un tastierino numerico con tasti da 1 a 9
e dovrà essere dotato della seguente funzionalità:
I. Pressione di ogni tasto con indicazione del numero di canale selezionato;
alla pressione di un tasto, nella corrispondente posizione del tastierino,
il numero dovrà essere sostituito dal carattere "P" (premuto)
Utilizzare le funzionalità della classe nell'ambito del medesimo script mediante input console che offra,
all'utente, la possibilità di premere i vari tasti del telecomando.
"""

class Telecomando:

    tasti = [0,1,2,3,4,5,6,7,8,9]

    def __repr__(self):
        return (f'{self.tasti[1]} {self.tasti[2]} {self.tasti[3]}\n{self.tasti[4]} {self.tasti[5]} {self.tasti[6]}\n'
                f'{self.tasti[7]} {self.tasti[8]} {self.tasti[9]}\n  {self.tasti[0]}')

    def pressione_tasto(self, tasto):
        Telecomando.tasti[tasto] = 'P'

telecomando = Telecomando()
print(telecomando)
canale = []

while True:
    tasto_scelto = input('\nChe canale vuoi vedere? Digita il numero del canale (Oppure OK per uscire): ')
    if tasto_scelto.upper() == "OK":
        print(f'Canale scelto: {canale}\nBuona visione')
        exit(3)
    else:
        tasto_scelto = int(tasto_scelto)
        canale.append(tasto_scelto)
        telecomando.pressione_tasto(tasto_scelto)
        print(telecomando)