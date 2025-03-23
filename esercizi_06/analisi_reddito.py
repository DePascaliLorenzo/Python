"""
Analizza il dataset "people.csv" allegato per individuare
la correlazione più significativa tra le variabili presenti e la variabile target.
L'obiettivo finale consiste nell'ottenimento dei dati di correlazione e del relativo grafico.
"""

from machine_learning.analisi.modello_base import ModelloBase
import pandas as pd
from scipy.stats import chi2_contingency,contingency,spearmanr
import matplotlib.pyplot as plt

_DATASET_PATH = '06. people.csv'
_DATASET_PATH_FIXED = '06.people_sistemato.csv'
label_old = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','target']
label_new = ['Età', 'Categoria di Lavoro','Peso Campionario','Educazione','Anni di Studio','Stato Coniugale','Mansione',
            'Relazione','Razza','Sesso','Entrate','Uscite','Ore Settimanali','Paese d\'Origine','Obiettivo']
drop_list_old = [label_old[2], label_old[4], label_old[14]]

class ModelloReddito(ModelloBase):

    def __init__(self, dataset_path):
        self.contingenza_razza = None
        self.dataframe = pd.read_csv(dataset_path)
        self.dataframe_sistemato = self.sistemazione_dataframe()

    def sistemazione_dataframe(self):

        df_sistemato = self.dataframe
        for i in range (len(label_new)):
            df_sistemato = df_sistemato.rename(columns = {
                label_old[i] : label_new[i]
            })

        return df_sistemato

    def tabella_contingenza(self,column, target):

        # self.dataframe_sistemato[target] = self.dataframe_sistemato.groupby(column)[target].transform('count')

        # generazione e stampa tabella di contingenza
        tabella_contingenza = pd.crosstab(self.dataframe_sistemato[column], self.dataframe_sistemato[target])

        print(f'TABELLA DI CONTINGENZA {column} - {target}: ', tabella_contingenza, sep='\n')
        # test chi quadro e stampa esito
        chi2, p, dof, expected = chi2_contingency(tabella_contingenza)
        print(f'Il p-value risultante dal test chi quadro sulla tabella di contingenza {column} - {target} è: {p}')
        print(f'Notazione non scientifica del p-value: {format(p, '.53f')}') #limite massimo decimali
        # calcolo indice di Cramer e stampa del valore
        cramer = contingency.association(tabella_contingenza, method='cramer')
        # pearson si sarebbe usato se le variabili fossero state quantitative

        print(f'L\'indice di Cramer calcolato sulla tabella di contingenza {column} - {target} è pari a: {cramer}')

        # di base da 0 a 0.1 è una correlazione debole, da 0.1 a 0.3 è una correlazione bassa, da 0.3 a 0.5 è una correlazione moderata
        # da 0.5 a 0.7 è una correlazione alta, da 0.7 a 0.9 è una correlazione molto alta, da 0.9 a 1 è una correlazione perfetta

        return tabella_contingenza

    def correlazione_spearman(self, column, target):
        spearman_corr, p = spearmanr(self.dataframe_sistemato[column], self.dataframe_sistemato[target])
        print(f'La correlazione di Spearman risultante tra {column} e {target} risulta pari a: {spearman_corr}')
        print(f'Il p-value risultante dal test chi quadro sulla tabella di contingenza {column} - {target} è: {p}')

    # metodo per generare grafici a barre partendo da tabelle contingenza
    def grafici_contingenza(self):
        # generazione figura
        figura, cella = plt.subplots(1,2, figsize = (12,5))
        # 1o grafico - sopravvivenza per classe
        self.contingenza_razza.plot(kind='bar', ax=cella[0], color = ['red','green'])
        cella[0].set_title('Frequenza di Sopravvivenza per Classe Passeggero')
        cella[0].set_xlabel('Classe Passeggero')
        cella[0].set_ylabel('Frequenza')
        cella[0].legend(title='legenda')
        cella[0].tick_params(axis = 'x', rotation = 0) # disposizione etichette asse x in orizzontale
        # 2o grafico - sopravvivenza per genere
        self.contingenza_razza.plot(kind='bar', ax=cella[1], color=['red', 'green'])
        cella[1].set_title('Frequenza di Sopravvivenza per Genere Passeggero')
        cella[1].set_xlabel('Genere dei Sopravvissuti')
        cella[1].set_ylabel('Frequenza')
        cella[1].legend(title='legenda')
        cella[1].tick_params(axis='x', rotation=0)  # disposizione etichette asse x in orizzontale

        # show della figura
        plt.tight_layout() # aggiustamento spazi per evitare sovrapposizioni
        plt.show()

    # metodo per generare grafico a dispersione per dimostrare correlazione di SPearman
    def grafico_spearman(self):
        # generazione figura
        plt.figure(figsize=(8,5))
        # grafico unico (asse x = età, asse y = sopravvivenza)
        plt.scatter(self.dataframe_sistemato[label_new[9]], self.dataframe_sistemato[label_new[14]], alpha = 0.5, color = 'blue')
        plt.title('Distribuzione Età vs Sopravvivenza')
        plt.xlabel('Età del Passeggero')
        plt.ylabel('Sopravvissuto (0 = No - 1= Sì)')
        plt.show()

    # metodo per generare grafico a torta per ripartizione sopravvissuti-deceduti
    def grafico_ripartizione(self):
        # conteggio generale osservazioni
        sopravvissuti_deceduti = self.dataframe_sistemato[label_new[14]].value_counts()
        sopravvissuti_deceduti.plot(kind = 'pie', autopct = '%1.1f%%', startangle=90, colors=['red','green'],
                                    labels = sopravvissuti_deceduti.index.map({0:'Deceduti',1:'Sopravvissuti'}))
        plt.title('Distribuzione Sopravvissuti-Deceduti')
        plt.ylabel('')
        # show del grafico
        plt.show()

modello = ModelloReddito(_DATASET_PATH)
# modello.analisi_generali(modello.dataframe_sistemato)
modello.dataframe_sistemato.to_csv(_DATASET_PATH_FIXED, index = False)
modello.analisi_valori_univoci(modello.dataframe_sistemato)
modello.contingenza_razza = modello.tabella_contingenza(label_new[9], label_new[14])
modello.correlazione_spearman(label_new[9], label_new[14])
modello.grafici_contingenza()
modello.grafico_spearman()
modello.grafico_ripartizione()
