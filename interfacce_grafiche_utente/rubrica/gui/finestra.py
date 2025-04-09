import tkinter as tk

import interfacce_grafiche_utente.rubrica.gui.finestra_due
from interfacce_grafiche_utente.rubrica.repository.contatto_repository import *
from tkinter import ttk
from tkinter.messagebox import askyesno
from interfacce_grafiche_utente.rubrica.gui.finestra_due import FinestraDue

class Finestra(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Applicazione Rubrica')
        self.geometry(f'600x600+{(self.winfo_screenwidth() - 600) // 2}+{(self.winfo_screenheight() - 600) // 2}')
        self.frame = self.generazione_frame()
        self.tabella = self.generazione_tabella()
        self.popolamento_tabella()
        self.config(menu = self.generazione_menu())

    def generazione_frame(self):
        frame = tk.Frame(master = self)
        frame.pack(fill = tk.BOTH, expand = True)
        return frame

    # metodo per generazione tabella visualizzazione dati
    def generazione_tabella(self):
        # scrollbar verticale
        scroll = tk.Scrollbar(master = self.frame)
        scroll.pack(side=tk.RIGHT, expand= tk.Y)
        # tabella di visualizzazione e il setting della scrollbar
        tabella = ttk.Treeview(master=self.frame, yscrollcommand=scroll.set, columns=('nome', 'cognome', 'telefono'))
        tabella.pack(fill=tk.Y, expand=True)
        scroll.config(command=tabella.yview)
        # definizione colonne (struttura generale della tabella)
        tabella.column('#0', width=0,stretch=tk.NO)
        tabella.column('nome', width=200, stretch=tk.NO)
        tabella.column('cognome', width=200, stretch=tk.NO)
        tabella.column('telefono', width=170, stretch=tk.NO, anchor=tk.CENTER)
        # impostazione header tabella
        tabella.heading('#0', text = '')
        tabella.heading('nome', text = 'Nome Contatto')
        tabella.heading('cognome', text = 'Cognome Contatto')
        tabella.heading('telefono', text = 'N° Telefono Contatto')
        # stilizzazione header tabella
        style = ttk.Style(master=self)
        style.theme_use('default')
        style.configure('Treeview.heading', background = 'lightgray')
        return tabella

    # metodo di logica per popolamento tabella
    def popolamento_tabella(self):
        # reset tabella
        for riga in self.tabella.get_children():
            self.tabella.delete(riga)
        # ottenimento lista contatto dal file e conversione da Contatto a list
        lista_contatti = elenco_contatti_repo()
        righe = [contatto.lista_attributi() for contatto in lista_contatti]
        # popolamento tabella
        for riga in righe:
            self.tabella.insert(parent = '', index = 'end', values = riga)

    # metodo per generazione barra menù
    def generazione_menu(self):
        barra = tk.Menu(master = self)
        item = tk.Menu(master = barra, tearoff = 0)
        item.add_command(label = 'Nuovo', command = self.aggiunta_contatto)
        item.add_command(label = 'Elimina', command = self.eliminazione_contatto)
        barra.add_cascade(label = 'File', menu = item)
        return barra

    def aggiunta_contatto(self):
        FinestraDue(self)

    def eliminazione_contatto(self):
        print(self.tabella.selection())
        if self.tabella.selection():
            riga_selezionata = self.tabella.item(self.tabella.selection()[0], 'values')
            print(riga_selezionata)
            conferma = askyesno(title='CONFERMA ELIMINAZIONE',
                                message=f'Sei sicuro di eliminare {riga_selezionata[1]}?',
                                parent=self)
            if conferma:
                contatto = Contatto(riga_selezionata[0], riga_selezionata[1], riga_selezionata[2])
                if eliminazione_contatto_repo(contatto):
                    self.popolamento_tabella()
