import threading
import time


main_thread = threading.main_thread()

# funzione target per definire il compito di un thread secondario
def compito_thread_uno(nome):
    print(f'Salve, sono il thread secondario {nome}')

# classe di modellazione oggetto di tipo Thread
class ThreadDue(threading.Thread):

    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    def run(self):
        for i in range(1,11):
            time.sleep(1)
            print(f'Sono il thread {self.nome} e stampo il numero {i}')

# ESECUZIONE PROGRAMMA
# avvio programma
print(f'{main_thread.name} ha avviato il programma')

# istanziazione e comunicazione di avvio thread secondario uno
thread_uno = threading.Thread(target = compito_thread_uno, args = ('Mario',))
thread_uno.start() # non avvia il thread (comunichiamo allo scheduler che thread uno è pronto a partire)

# istanziazione e comunicazione di avvio thread secondario due
thread_due = ThreadDue('Gianni')
thread_due.start()
thread_due.join()

# istanziazione e comunicazione di avvio thread secondario due
nomi_thread = ['Laura', 'Sara', 'Roberta']
vari_thread = [ThreadDue(nome) for nome in nomi_thread]
for thread in vari_thread:
    thread.start()
    thread.join()

# termine programma
print(f'{main_thread.name} ha terminato il programma')