from prodotto import Prodotto
import unittest

# classe con funzionalità di test automatizzate
class TestProdotto(unittest.TestCase):

    # metodo per testare la validità delle informazioni Prodotto in fase di creazione
    # obiettivo: verificare che nome eprezzo del Prodotto vengano valorizzati correttamente
    def test_istanziazione(self):
        prodotto = Prodotto('Penna', 1.5)
        self.assertEqual(prodotto.nome, 'Penna')
        self.assertEqual(prodotto.prezzo, 1.5)

    # metodo per testare creazione di Prodotto con valore non numerico o inferiore a 1
    # obiettivo: verificare che venga lanciato un ValueError con un determinato messaggio
    def test_prezzo_sbagliato(self):
        with self.assertRaises(ValueError) as context:
            Prodotto('Penna', 0.9)
        self.assertEqual(str(context.exception), 'Il prezzo deve essere un numero non inferiore di 1')