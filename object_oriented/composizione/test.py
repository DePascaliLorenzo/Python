from object_oriented.composizione.model.camera import Camera
from object_oriented.composizione.model.cliente import Cliente
from object_oriented.composizione.model.prenotazione import Prenotazione

# funzione per creare una Camera
def creazione_camera():
    return Camera(103, "Matrimoniale", 89.55)

# funzione per creare un Cliente
def registrazione_cliente():
    nome = input('Inserire nome cliente: ')
    cognome = input('Inserire cognome cliente: ')
    cliente = Cliente(nome, cognome)
    print(f'{cliente} registrato con successo!')
    return cliente

# funzione per registrare una Prenotazione
def registrazione_prenotazione():
    # ottenimento camera (unica disponibile)
    camera = creazione_camera()
    # arriva la telefonata del Cliente
    cliente = registrazione_cliente()
    data_arrivo = input('Inserire data arrivo in formato gg-mm-aaaa: ')
    data_partenza = input('Inserire data partenza in formato gg-mm-aaaa: ')
    #registrazione della Prenotazione
    print('')
    prenotazione = Prenotazione(data_arrivo, data_partenza, cliente, camera)
    print(prenotazione, 'Prenotazione registrata con successo', sep='\n')

# invocazione funzione di avvio

registrazione_prenotazione()
