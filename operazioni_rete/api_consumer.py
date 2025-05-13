import requests

# definizione classe di modellazione oggetto logico Post
class Post:

    # metodo di inizializzazione
    def __init__(self,id = None, title=None, body=None, userId=None):
        self.id = id
        self.title = title
        self.body = body
        self.userId = userId

    # metodo di rappresentazione testuale
    def __repr__(self):
        return f"Post Id: {self.id}\nId Utente: {self.userId}\nTitolo: {self.title}\nContenuto: {self.body}\n"

    # metodo di deserializzazione (oggetto json -> oggetto Python di tipo Post)
    @classmethod
    def deserializzazione(cls,json):
        return cls(**json)

    # metodo di serializzazione (oggetto Python di tipo Post -> oggetto json)
    def serializzazione(self):
        return self.__dict__

# funzione per acquisizione dati da un web service

def acquisizione_dati():
    try:
        # invio richiesta e ottenimento risposta
        risposta = requests.get('https://jsonplaceholder.typicode.com/posts')
        print(risposta)
        # analisi dati ricevuti
        dati_ricevuti = risposta.json()
        print(dati_ricevuti, type(dati_ricevuti))
        print(dati_ricevuti[0], type(dati_ricevuti[0]))
        print(dati_ricevuti[0]['title'])
        # trasformazione da lista di dizionari a lista di oggetti Python di tipo Post
        lista_post = [Post.deserializzazione(dato) for dato in dati_ricevuti]
        for post in lista_post:
            print(post)
    except Exception as e:
        print(e)

# funzione per invio dati ad un web service
def invio_dati():
    # creazione oggetto Post con dati recuperati dall'utente
    post = Post(title = "Il mio primo post", body = 'Contenuto del mio post', userId = 23)
    try:
        # invio richiesta e ottenimento risposta
        risposta = requests.post('https://jsonplaceholder.typicode.com/posts', post.serializzazione())
        print(risposta.json())
    except Exception as e:
        print(e)


# invocazione funzioni
# acquisizione_dati()
invio_dati()