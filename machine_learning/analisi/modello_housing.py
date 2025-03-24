import numpy as np
from modello_base import ModelloBase
import pandas as pd
from datetime import datetime
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

_DATASET_PATH = "../dataset/data_05.csv"

class ModelloHousing(ModelloBase):

    # meotodo di inizializzazione
    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.dataframe_sistemato, self.scaler = self.sistemazione_dataframe()
        # self.individuazione_correlazioni()
        # self.regressione_lineare_semplice()
        self.regressione = self.regressione_lineare_multipla()

    def sistemazione_dataframe(self):
        # 1. copia del dataframe
        df_sistemato = self.dataframe.copy()
        # 2. sostituzione outliers con limiti
        colonne_con_outliers =['Distanza_Metro_m', 'Distanza_Tangenziale_m']
        for col in colonne_con_outliers:
            q1 = df_sistemato[col].quantile(0.25)
            q3 = df_sistemato[col].quantile(0.75)
            iqr = q3-q1
            limite_inferiore = q1 - 1.5 * iqr
            limite_superiore = q3 + 1.5 * iqr
            df_sistemato[col] = np.where(df_sistemato[col] < limite_inferiore, limite_inferiore, df_sistemato[col])
            df_sistemato[col] = np.where(df_sistemato[col] > limite_superiore, limite_superiore, df_sistemato[col])

        # 3. sostituzione colonna Anno_Costruzione con colonna Età_Immobile
        df_sistemato['Età_Immobile'] = datetime.now().year - df_sistemato['Anno_Costruzione']
        df_sistemato = df_sistemato.drop(['Anno_Costruzione'], axis = 1)

        # 4. scaling colonne variabili
        colonne_da_scalare = df_sistemato.drop(['Prezzo_Vendita'], axis = 1)
        scaler = StandardScaler()
        colonne_scalate = scaler.fit_transform(colonne_da_scalare)
        df_scalato = pd.DataFrame(colonne_scalate, columns = colonne_da_scalare.columns)
        df_sistemato = pd.concat([df_scalato, df_sistemato['Prezzo_Vendita']], axis = 1)

        return df_sistemato, scaler

    # metodo per individuazione delle correlazioni
    def individuazione_correlazioni(self):
        matrice_correlazione = self.dataframe_sistemato.corr()
        print('***** MATRICE DI CORRELAZIONE *****', matrice_correlazione.to_string(), sep = '\n')
        # generazione heatmap correlazioni
        plt.figure(figsize=(12,12))
        sns.heatmap(matrice_correlazione, annot = True, cmap = 'coolwarm', fmt = '.2f', linewidth = 0.5)
        plt.xticks(rotation = 30, ha = 'right')
        plt.title('Heatmap delle Correlazioni')
        plt.show()
        # controllo delle correlazioni
        self.verifica_correlazioni()

    # metodo per conferma correlazioni variabili
    def verifica_correlazioni(self):
        # predisposizione dizionario per informazioni
        risultati_verifica = {
            'variabile': [],
            'correlazione': [],
            'p-value': [],
            'p-value-ns': []
        }
        # popolamento dizionario
        for col in self.dataframe_sistemato.columns:
            if col != 'Prezzo_Vendita':
                corr, p = pearsonr(self.dataframe_sistemato[col], self.dataframe_sistemato['Prezzo_Vendita'])
                risultati_verifica['variabile'].append(col)
                risultati_verifica['correlazione'].append(corr)
                risultati_verifica['p-value'].append(p)
                risultati_verifica['p-value-ns'].append(format(p,'.53f'))

        # trasformazione dizionario in dataframe
        df_correlazione = pd.DataFrame(risultati_verifica)
        print('***** CORRELAZIONI VARIABILI-TARGET *****', df_correlazione.to_string(), sep = '\n')

    # metodo per determinare regressione lineare semplice tra superficie_mq e prezzo_vendita
    def regressione_lineare_semplice(self):
        # definizione target e regressore
        y = self.dataframe_sistemato[['Prezzo_Vendita']].values.reshape(-1,1) # target
        x = self.dataframe_sistemato[['Superficie_mq']].values.reshape(-1,1) # regressore
        # creazione e addestramento (semplificato) del modello di regressione
        regressione = LinearRegression()
        regressione.fit(x,y)
        # ottenimento punteggio del modello (vicino a 1 -> modello ok)
        print('***** PUNTEGGIO MODELLO REGRESSIONE *****', regressione.score(x,y), sep = '\n')
        # ottenimento retta di regressione
        retta_regressione = regressione.predict(x)
        # reinversione valori standardizzati colonna Superficie_mq
        col_index = self.dataframe_sistemato.columns.get_loc('Superficie_mq') # ottenimento indice colonna
        x_reali = (x * self.scaler.scale_[col_index] + self.scaler.mean_[col_index]) # formula inversa di standardizzazione

        # grafico modello
        plt.scatter(x_reali, y, label = 'Osservazioni', s = 3, color = 'blue')
        plt.plot(x_reali, retta_regressione, color = 'red', label = 'Regressione Lineare', linewidth = 1.1)
        plt.title('Regressione Lineare tra Superficie e Prezzo di Vendita')
        plt.xlabel('Superficie (mq)')
        plt.ylabel('Prezzo di Vendita')
        plt.show()

    # metodo per determinare regressione lineare multipla e ottenere modello predittivo
    def regressione_lineare_multipla(self):
        # definizione di target e regressori
        regressori = self.dataframe_sistemato.drop(['Prezzo_Vendita'], axis = 1).columns
        y = self.dataframe_sistemato[['Prezzo_Vendita']].values.reshape(-1,1)
        x = self.dataframe_sistemato[regressori]
        # suddivisione delle osservazioni in addestramento (80%) e test (20%)
        x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2,random_state=42)
        # creazione e addestramento del modello di regressione
        regressione = LinearRegression()
        regressione.fit(x_train,y_train)
        # predizioni del modello
        y_pred_train = regressione.predict(x_train)
        y_pred_test = regressione.predict(x_test)
        # valutazione del modello
        print('***** VALUTAZIONE MODELLO *****')
        print(f'Punteggio del modello (test): {regressione.score(x_train,y_train):.4f}')
        print(f'Punteggio del modello (train): {regressione.score(x_test,y_test):.4f}')
        print(f'Errore Assoluto Medio (test): {mean_absolute_error(y_test,y_pred_test):.2f} €')
        print(f'Errore Assoluto Medio (train): {mean_absolute_error(y_train,y_pred_train):.2f} €')
        print(f'Errore Quadratico Medio (test): {np.sqrt(mean_squared_error(y_test,y_pred_test)):.2f} €')
        print(f'Errore Quadratico Medio (train): {np.sqrt(mean_squared_error(y_train,y_pred_train)):.2f} €')
        # istogramam distribuzione errori di predizione (in fase di test)
        errori = y_test.flatten() - y_pred_test.flatten() # differenza tra prezzi reali e predetti
        plt.figure(figsize = (10,6))
        plt.hist(errori, bins = 50, color = 'red', alpha = 0.7, edgecolor = 'black')
        plt.axvline(x = 0, color = 'blue', linestyle = 'dashed', linewidth = 1.5)
        plt.title('Distribuzione Errori di Predizione')
        plt.xlabel('Errore (Prezzo Reale - Prezzo Predetto) in Euro')
        plt.ylabel('Numero di Immobili')
        plt.show()
        # I risultati a sinistra della linea verticale evidenzia una sovrastima, a destra invece ci sono le sottostime
        return regressione

    # metodo per predire il valore di un immobile (partendo dai suoi dati)
    def predizione_valore(self, immobile):
        # creazione DataFrame per un nuovo immobile
        df_immobile = pd.DataFrame([immobile]) # singola osservazione quindi parentesi quadre
        # standardizzazione variabili mediante scaler utilizzato per il modello
        df_immobile_scalato = self.scaler.transform(df_immobile)
        df_immobile_scalato = pd.DataFrame(df_immobile_scalato, columns = df_immobile.columns)
        # predizione del prezzo mediante modello addestrato
        prezzo_predetto = self.regressione.predict(df_immobile_scalato)[0][0]
        # stampa risultato
        print(f'***** Prezzo Predetto per il nuovo immobile: {prezzo_predetto:.2f} € *****')

# utilizzo modello
modello = ModelloHousing(_DATASET_PATH)
modello.analisi_generali(modello.dataframe_sistemato)
modello.analisi_indici_statistici(modello.dataframe_sistemato)
modello.individuazione_outliers(modello.dataframe_sistemato)

# predizione prezzo per un nuovo immobile
nuovo_immobile = {
    "Superficie_mq": 85,
    "Num_Camere": 3,
    "Num_Bagni": 2,
    "Piano": 4,
    "Distanza_Metro_m": 500,
    "Rumorosita_Area_dB": 45,
    "Distanza_Tangenziale_m": 2500,
    "Età_Immobile": 20
}
modello.predizione_valore(nuovo_immobile)