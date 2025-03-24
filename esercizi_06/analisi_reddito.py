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
#              0        1          2        3           4                   5           6               7           8     9       10            11                  12              13          14
label_old = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','target']
label_new = ['Età', 'Categoria di Lavoro','Peso Campionario','Educazione','N° Educazione','Stato Coniugale','Mansione',
            'Relazione','Razza','Sesso','Entrate','Uscite','Ore Settimanali','Paese d\'Origine','Obiettivo']
drop_list_new = [label_new[2],label_new[4],label_new[11]]

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
        df_sistemato = df_sistemato.drop(drop_list_new, axis=1)
        df_sistemato[label_new[1]] = df_sistemato[label_new[1]].map(lambda x: None if x == '?' else x)
        df_sistemato[label_new[6]] = df_sistemato[label_new[6]].map(lambda x: None if x == '?' else x)
        df_sistemato[label_new[13]] = df_sistemato[label_new[13]].map(lambda x: None if x == '?' else x)

        return df_sistemato

    def tabella_contingenza(self,column, target):

        tabella_contingenza = pd.crosstab(self.dataframe_sistemato[column], self.dataframe_sistemato[target])

        print(f'TABELLA DI CONTINGENZA {column} - {target}: ', tabella_contingenza, sep='\n')
        chi2, p, dof, expected = chi2_contingency(tabella_contingenza)
        print(f'Il p-value risultante dal test chi quadro sulla tabella di contingenza {column} - {target} è: {p}')
        print(f'Notazione non scientifica del p-value: {format(p, '.53f')}')
        cramer = contingency.association(tabella_contingenza, method='cramer')
        print(f'L\'indice di Cramer calcolato sulla tabella di contingenza {column} - {target} è pari a: {cramer}')

        return tabella_contingenza

    def correlazione_spearman(self, column, target):
        spearman_corr, p = spearmanr(self.dataframe_sistemato[column], self.dataframe_sistemato[target])
        print(f'La correlazione di Spearman risultante tra {column} e {target} risulta pari a: {spearman_corr}')
        print(f'Il p-value risultante dal test chi quadro sulla tabella di contingenza {column} - {target} è: {p}')

    def grafici_contingenza(self):

        figura, cella = plt.subplots(figsize=(6, 5))  # Rimuove la suddivisione in due celle
        self.contingenza_razza.plot(kind='bar', ax=cella, color=['red', 'green'])
        cella.set_title('Frequenza di Obiettivo per Razza')
        cella.set_xlabel('Razza')
        cella.set_ylabel('Obiettivo')
        cella.legend(title='legenda')
        cella.tick_params(axis = 'x', rotation = 0)

        plt.tight_layout()
        plt.show()

    def grafico_ripartizione(self):
        conteggio = self.dataframe_sistemato[label_new[14]].value_counts()
        conteggio.plot(kind = 'pie', autopct = '%1.1f%%', startangle=90, colors=['red','green'],
                                    labels = conteggio.index.map({'<=50K':'<=50K','>50K':'>50K'}))
        plt.title('Distribuzione Sopravvissuti-Deceduti')
        plt.legend(title = 'legenda')
        plt.ylabel('')
        plt.show()

modello = ModelloReddito(_DATASET_PATH)
modello.contingenza_razza = modello.tabella_contingenza(label_new[7], label_new[14])
modello.correlazione_spearman(label_new[10], label_new[14])
modello.grafici_contingenza()
modello.grafico_ripartizione()
modello.dataframe_sistemato.to_csv(_DATASET_PATH_FIXED, index = False)
