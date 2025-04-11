import threading
import time

# funzione target per compito thread secondario (archiviazione)
def archiviazione():
    try:
        with open('file.txt', 'a') as file:
            file.write('a' * 1_000_000_000)
            print(f'Archiviazione terminata alle {time.time()}')
    except Exception as e:
        print(e)


print(f'Avvio programma alle {time.time()}')

# istanziazione e comunicazione di avvio thread secondario di archiviazione
thread_archiviazione = threading.Thread(target=archiviazione)
thread_archiviazione.start()

# liberazione programma
print('Adesso procedi con la prossima operazione')