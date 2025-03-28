"""
Realizzare, sfruttando il paradigma Object Oriented e le specifiche del modulo tkinter,
un applicativo dotato di interfaccia grafica che permetta di convertire
un valore indicato dall'utente in metri nelle corrispondenti misure espresse in pollici e miglia.
Il software dovrà anche prevedere una modalità di reset
e si raccomanda di prestare particolare attenzione alla prevenzione di potenziali eccezioni.
"""

import tkinter as tk

class Convertitore(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Convertitore')
        self.geometry(f'600x600+{(self.winfo_screenwidth()-600)//2}+{(self.winfo_screenheight()-600)//2}')
        self.frame = self.generazione_contenitore()
        self.label, self.entry, self.button, self.label_pollici, self.label_miglia = self.generazione_elementi()

    def generazione_contenitore(self):
        frame = tk.Frame(master=self, background='grey')
        frame.pack(expand=True, fill=tk.BOTH)
        return frame

    def generazione_elementi(self):
        label = tk.Label(master=self.frame, text="Inserire il Valore da Convertire:", font="Arial 12 bold", background="grey",
                         foreground="black")
        # posiziono la label in mezzo alla finestra
        label.place(x=250, y=320, width=300, height=25)

        entry = tk.Entry(master=self.frame, font="Arial 12", background="white", foreground="black", justify='center')
        entry.place(x=250, y=360, width=300, height=30)

        button = tk.Button(master=self.frame, text="Converti", font="Arial 12", background="white", foreground="black", command = self.conversione)
        button.place(x=250, y=400, width=300, height=30)

        label_pollici = tk.Label(master=self.frame, text = 'pollici',  font="Arial 12 bold", background="grey", foreground="black")
        label_pollici.place(x=250, y=450)

        label_miglia = tk.Label(master=self.frame, text = 'miglia',  font="Arial 12 bold", background="grey", foreground="black")
        label_miglia.place(x=250, y=500)

        button_reset = tk.Button(master=self.frame, text = 'RESET', font='Arial 12 bold', background='white', foreground='black', command = self.reset)
        button_reset.place(x=0, y=0, width=300, height=30)

        return label, entry, button, label_pollici, label_miglia

    def conversione(self):
        try:
            # pollici = metri * 39.3701
            pollici = float(self.entry.get()) * 39.3701
            # miglia = metri / 1609.34
            miglia = float(self.entry.get()) / 1609.34
            self.label_pollici.config(text = f'Pollici: {pollici:.2f}"')
            self.label_miglia.config(text = f'Miglia: {miglia:.5f}')
        except Exception:
            self.label_pollici.config(text = 'Pollici: Errore')
            self.label_miglia.config(text = 'Miglia: Errore')

    def reset(self):
        self.label_pollici.config(text='Pollici')
        self.label_miglia.config(text='Miglia')
        self.entry.delete(0, tk.END)


Convertitore().mainloop()