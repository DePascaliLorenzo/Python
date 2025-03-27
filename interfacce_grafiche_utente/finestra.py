import tkinter as tk

class Finestra(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Finestra Programma')
        self.geometry('600x600+300+50') #('larghezzaxaltezza+X+y')
        self.geometry(f'600x600+{(self.winfo_screenwidth() - 600) // 2}+{(self.winfo_screenheight() - 600) // 2}')
        self.state('zoomed')

Finestra().mainloop()