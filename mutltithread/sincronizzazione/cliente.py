import threading
import random
import time
from time import sleep


class Cliente(threading.Thread):

    # attrinuto di classe per rappresentare la lista d'attesa
    lista_attesa = []

    def __init__(self, nome, negozio):
        super().__init__()
        self.nome = nome
        self.negozio = negozio

    def __repr__(self):
        return self.nome

    # ovverride metodo da superclasse Thread per assegnazione compito
    def run(self):
        tempo_casuale = random.randint(5,15)
        self.negozio.ingresso(self)
        Cliente.lista_attesa.remove(self)
        print(f'Clienti in attesa: {Cliente.lista_attesa}\nTempo d\'attesa: {tempo_casuale}') if len(Cliente.lista_attesa) > 0 else print('Non rimane nessuno in attesa')
        sleep(tempo_casuale)
        self.negozio.uscita(self)