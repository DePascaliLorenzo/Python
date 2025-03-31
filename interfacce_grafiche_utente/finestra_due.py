import tkinter as tk
from tkinter import ttk
from calendar import month_name

class FinestraDue(tk.Toplevel):

    def __init__(self, principale):
        super().__init__(master=principale)
        self.title('Finestra Secondaria')
        self.geometry(f'400x400+{(principale.winfo_width() - 400) // 2}+{(principale.winfo_height() - 400) // 2}')
        self.contenitore = self.generazione_contenitore()
        # gestione check singolo
        self.controllo_check_singolo = tk.BooleanVar()
        self.check_singolo = self.generazione_check_singolo()
        # gestione check multipli
        self.schema_check_multipli = {
            'Cinema': tk.BooleanVar(),
            'Musica': tk.BooleanVar(),
            'Teatro': tk.BooleanVar()
        }
        self.check_multipli = self.generazione_check_multipli(60)
        # gestione radiobutton
        self.controllo_genere = tk.StringVar()
        self.controllo_genere.set('Uomo') # Default value
        self.generazione_radiobutton()
        # gestione combobox
        self.combobox = self.generazione_combobox()

    def generazione_contenitore(self):
        frame = tk.Frame(master=self)
        frame.pack(fill=tk.BOTH, expand=True)
        return frame

    # metodo generazione di un singolo check
    def generazione_check_singolo(self):
        check = tk.Checkbutton(master=self.contenitore, text='Accetta la Privacy', command=self.selezione_check_singolo, variable=self.controllo_check_singolo)
        check.place(x=20,y=20,width=200,height=25)
        return check

    # metodo di logica invocato a selezione/deselezione del check singolo
    def selezione_check_singolo(self):
        print('Azione registrata sul check singolo')
        if self.controllo_check_singolo.get():
            print('Il check è selezionato')
        else:
            print('Il check non è selezionato')

    # metodo per generazione gruppo di check
    def generazione_check_multipli(self,posizione_y):
        lista_check = []
        for testo, variabile in self.schema_check_multipli.items():
            check = tk.Checkbutton(master=self.contenitore, text = testo, variable=variabile)
            check.place(x=20, y=posizione_y, width = 200, height = 25)
            posizione_y += 25
            lista_check.append((check, variabile))
        # pulsante di servizio (tanto per generare l'evento)
        button = tk.Button(master=self.contenitore, text='Invia', command= self.recupero_stati_check_multipli)
        button.place(x = 20, y = 140, width=100, height=25)
        return lista_check

    # metodo di logica invocato al click sul button dei check multipli (recupero preferenze)
    def recupero_stati_check_multipli(self):
        preferenze_utente = []
        for check, variabile_controllo in self.check_multipli:
            if variabile_controllo.get():
                preferenze_utente.append(check['text'])
        print(preferenze_utente)

    # metodo per generazione di 2 radiobutton (Uomo/Donna)
    def generazione_radiobutton(self):
        radio_uomo = tk.Radiobutton(master=self.contenitore, text='uomo', value='Uomo', variable=self.controllo_genere)
        radio_uomo.place(x=20, y=180, width=200, height=25)
        radio_donna = tk.Radiobutton(master=self.contenitore, text = 'donna', value='Donna', variable=self.controllo_genere)
        radio_donna.place(x=20,y=205, width=200,height=25)
        # pulsante di servizio (tanto per generare l'evento
        button = tk.Button(master=self.contenitore, text='Invia', command = self.recupero_selezione_radio)
        button.place(x = 20, y = 240, width=100, height=25)

    # metodo di logica invocato al click sul button di servizio dei radio (recupero genere utente)
    def recupero_selezione_radio(self):
        print(f'L\'Utente è {self.controllo_genere.get()}')

    # metodo per generazione combobox (select in ambito web)
    def generazione_combobox(self):
        lista_mesi = [month_name[mese] for mese in range(1,13)]
        combo = ttk.Combobox(master=self.contenitore, state = 'readonly', values=lista_mesi)
        combo.set('Scegli il mese')
        combo.bind('<<ComboboxSelected>>', self.selezione_item_combo)
        combo.place(x = 20, y = 270, width = 200, height = 25)
        # pulsante di servizio tanto per generare l'evento
        button = tk.Button(master=self.contenitore, text = 'Invia', command=self.controllo_item_combo)
        button.place(x=20,y=320,width=100,height=25)
        return combo

    # metodo di logica attivato alla selezione di ogni item del combobox
    def selezione_item_combo(self, event):
        print(f'Selezionato il mese {self.combobox.get()}')

    # metodo di logica attivato al click sul button di servizio del combobox
    def controllo_item_combo(self):
        print(f'L\'utente è nato nel mese di {self.combobox.get()}')
