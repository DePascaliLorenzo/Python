import tkinter as tk
from finestra_due import FinestraDue

class Finestra(tk.Tk):

    # schema
    schema_menu ={
        'File': ['Apri','Nuovo','Salva', 'Nuova Finestra'],
        'Edit': ['Seleziona', 'Seleziona Tutto']
    }

    def __init__(self):
        super().__init__()
        self.title('Finestra Programma')
        self.geometry('600x600+300+50') #('larghezzaxaltezza+X+y')
        self.geometry(f'600x600+{(self.winfo_screenwidth() - 600) // 2}+{(self.winfo_screenheight() - 600) // 2}')
        # estensione a tutto schermo al momento del run
        self.state('zoomed')
        # generazione frame contenitore unico
        # self.generazione_contenitore()
        # generazione frame di sezione con rif
        self.laterale,self.superiore,self.inferiore,self.centrale = self.generazione_sezioni()
        # generazione componenti frame laterale
        self.label, self.entry, self.button, self.label_due = self.generazione_componenti_laterali()
        # configurazione barra menu
        self.config(menu=self.generazione_menu())

    # metodo per generazione di un frame contenitore
    def generazione_contenitore(self):
        frame = tk.Frame(master=self, background='lightyellow') # master = self lega il frame alla nostra finestra
        frame.pack(fill=tk.BOTH, expand=True)

    # metodo per generazione di 4 frame contenitori (sezioni interfaccia)
    def generazione_sezioni(self):
        laterale = tk.Frame(master=self, background='lightblue', width=300)
        superiore = tk.Frame(master=self, background='lightyellow', height=150)
        inferiore = tk.Frame(master=self, background='lightgreen', height=150)
        centrale = tk.Frame(master=self, background='lightgray', height=150)
        laterale.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)
        superiore.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        inferiore.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False)
        centrale.pack(fill=tk.BOTH, expand=True)
        return laterale,superiore,inferiore,centrale

    # metodo per generazione componenti frame laterale (label - caselle editabili - pulsanti)
    def generazione_componenti_laterali(self):
        label = tk.Label(master=self.laterale, text = 'Testo iniziale di default', background='lightblue', foreground='red', font= 'Arial 12 bold')
        label.bind('<Button-3>', self.ripristino_testo)
        label.place(x = 50, y = 30, width = 200, height = 25)
        # case editabile
        entry = tk.Entry(master=self.laterale, background='white', font = 'Arial 12')
        entry.place(x = 50, y = 65, width = 200, height = 25)
        entry.bind('<Key>', self.recupero_test)

        button = tk.Button(master=self.laterale, text ='Clicca Qui', background='black', foreground='white', font='Arial 12 bold', cursor = 'hand2', command=self.modifica_testo)
        button.place(x = 100, y = 100, width = 100, height = 25)

        label_due = tk.Label(master=self.laterale, background='lightblue', font = 'Arial 12 bold')
        label_due.place(x = 50, y = 140, width = 200, height = 25)

        return label,entry, button, label_due

    # metodo di logica attivato al click del pulsante
    def modifica_testo(self):
        self.label['text'] = self.entry.get() # recupero testo entry e sovrascrittura testo label
        self.entry.delete(0, tk.END) # reset completo testo entry

    # metodo di logica attivato al click mouse dx sulla label
    def ripristino_testo(self, event):
        self.label['text'] = 'Testo iniziale di default' # ripristino label a stato originale
        self.label_due['text'] = ''  # ripristino label_due a stato originale
        print(event)

    # metodo di logica attivato alla digitazione nella casella di input
    def recupero_test(self, event):
        if event.keysym != 'BackSpace':
            self.label_due['text'] += event.char
        else:
            self.label_due['text'] = self.label_due['text'][:-1]

    # metodo per generazione e popolamento barra menù
    def generazione_menu(self):
        # creazione barra menu
        barra_menu = tk.Menu(master=self)
        # generazione item principali
        for nome_item, lista_nomi_sottoitem in Finestra.schema_menu.items():
            item_menu = tk.Menu(master=barra_menu, tearoff=0)
            barra_menu.add_cascade(label=nome_item, menu=item_menu)
            # generazione sottoitem
            for nome_sottoitem in lista_nomi_sottoitem:
                item_menu.add_command(label=nome_sottoitem, command= lambda c=nome_sottoitem: self.gestione_menu(c))
        return barra_menu

    # metodo di logica per gestione generale dei comandi menu
    def gestione_menu(self, comando):
        # print(comando)
        if comando == 'Nuova Finestra':
            FinestraDue(self)

Finestra().mainloop()