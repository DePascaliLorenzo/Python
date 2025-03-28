import tkinter as tk

class FinestraDue(tk.Toplevel):

    def __init__(self, principale):
        super().__init__(master=principale)
        self.title('Finestra Secondaria')
        self.geometry(f'400x400+{(principale.winfo_width() - 400) // 2}+{(principale.winfo_height() - 400) // 2}')
        self.contenitore = self.generazione_contenitore()

    def generazione_contenitore(self):
        frame = tk.Frame(master=self)
        frame.pack(fill=tk.BOTH, expand=True)
        return frame