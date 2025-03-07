"""
CALCOLARE IL PIANO DI AMMORTAMENTO DI UN FINANZIAMENTO
(metodo calcolo italiano -> quota capitale costante e rata variabile)
Input utente:
- Importo finanziamento
- Durata finanziamento (in anni)
- Numero delle rate annuali (ad esempio 12 rate/anno)
- Tasso di interesse (ad esempio 5%)

Verifica input utente:
Conversione input utente in numerici
Calcolo effettivo
Stampa tabella del piano ammortamento (Rata n.  Totale Rata  Quota Interessi  Quota Capitale  Residuo Da Pagare)
"""

# funzione per acquisizione input utente
def acquisizione_input():
    importo_finanziamento = input('Inserisci importo del finanziamento: ').strip()
    durata_finanziamento = input('Inserisci la durata in anni: ').strip() # strip() per eliminare spazi bianchi
    rate_annuali = input('Inserisci il numero delle rate di rimborso annuali: ').strip()
    tasso_interesse = input('Inserisci il tasso di interesse (ad esempio 5 per 5%): ').strip()
    return importo_finanziamento, durata_finanziamento, rate_annuali, tasso_interesse

"""
ESTENSIONE DELLA LIST COMPREHENSION
convertiti = []
for valore in valori:
    convertiti.append(int(valore))
"""

# funzione per controllo e conversione sicura degli input
def conversione_input(valori): # riceve una tupla
    if all(valore.isnumeric() for valore in valori): # verifica che tutti i valori siano numerici
        convertiti = [int(valore) for valore in valori] # conversione sicura
        return convertiti
    else:
        return None

# funzione per calcolare il piano di ammortamento (lista bidimensionale)
def calcolo_piano_ammortamento(valori):
    # unpackaging della lista valori ricevuta in input
    importo, anni, rate_anno, tasso = valori
    # dati preliminari necessari per il calcolo
    totale_rate = anni * rate_anno
    tasso_effettivo = tasso / 100
    quota_capitale_rata = importo / totale_rate
    # definizione tabella piano ammortamento e riga di intestazione
    piano_ammortamento = [
        ['N° Rata', 'Totale Rata', 'Quota Interessi', 'Quota Capitale', 'Capitale Residuo']
    ]
    # popolamento tabella piano ammortamento
    for indice in range(1, totale_rate + 1):
        interessi_rata = ((importo * tasso_effettivo) * anni) / totale_rate
        totale_rata = quota_capitale_rata + interessi_rata
        capitale_residuo = importo - quota_capitale_rata
        riga_rata = [
            f'Rata n.{indice}',
            f'{totale_rata:.2f}',
            f'{interessi_rata:.2f}',
            f'{quota_capitale_rata:.2f}',
            f'{capitale_residuo:.2f}'
        ]
        piano_ammortamento.append(riga_rata)
        importo = capitale_residuo
    return piano_ammortamento

# funzione di avvio programma
def start():
    valori_acquisiti = conversione_input(acquisizione_input())
    if valori_acquisiti:
        piano_ammortamento = calcolo_piano_ammortamento(valori_acquisiti)
        print(piano_ammortamento)
        for riga in piano_ammortamento:
            print(riga)
    else:
        print('Hai sbagliato ad inserire qualche dato. Riavvia e riprova')

# invocazione funzione di avvio
start()