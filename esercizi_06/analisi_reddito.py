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
work_class_list = ['State-gov', 'Self-emp-not-inc', 'Private', 'Federal-gov', 'Local-gov', '?', 'Self-emp-inc', 'Without-pay', 'Never-worked',]

class ModelloReddito(ModelloBase):

    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.dataframe_sistemato = self.sistemazione_dataframe()
        self.contingenza_razza = self.tabella_contingenza(label_old[8], label_old[10])
        # self.contingenza_genere = self.tabella_contingenza('Genere', 'Sopravvissuto')
        # self.correlazione_spearman('Età','Sopravvissuto')
        # self.grafici_contingenza()
        # self.grafico_spearman()
        # self.grafico_ripartizione()

    def sistemazione_dataframe(self):

        df_sistemato = self.dataframe
        df_sistemato = df_sistemato.rename(columns = {
            label_old[0] : label_new[0],
            label_old[1] : label_new[1],
            label_old[3] : label_new[3],
            label_old[5] : label_new[5],
            label_old[6] : label_new[6],
            label_old[7] : label_new[7],
            label_old[8] : label_new[8],
            label_old[9] : label_new[9],
            label_old[10] : label_new[10],
            label_old[11] : label_new[11],
            label_old[12] : label_new[12],
            label_old[13] : label_new[13],
        })
        """
        # assegnazione valori numerici alla colonna Categoria di Lavoro
        df_sistemato[label_new[1]] = df_sistemato[label_new[1]].map({work_class_list[0]: '7', work_class_list[1]: '6',
                                                                     work_class_list[2]: '5', work_class_list[3]: '4',
                                                                     work_class_list[4]: '3', work_class_list[5]: None,
                                                                     work_class_list[6]: '2', work_class_list[7]: '1', work_class_list[8]: '0'})

        # assegnazione valori numerici alla colonna Mansione
        df_sistemato[label_new[6]] = df_sistemato[label_new[6]].map({'Priv-house-serv': '0', 'Handlers-cleaners': '1',
                                        'Farming-fishing': '2', 'Other-service': '3', 'Machine-op-inspct': '4', 'Transport-moving': '5',
                                        'Craft-repair': '6', 'Sales': '7', 'Tech-support': '8', 'Adm-clerical': '9', 'Protective-serv': '10',
                                        'Exec-managerial': '11', 'Prof-specialty': '12', 'Armed-Forces': '13', '?': None})
        """
        return df_sistemato

    def tabella_contingenza(self,column, target):
        tabella_contingenza = pd.crosstab(self.dataframe[column], self.dataframe[target])

        tabella_contingenza.columns = tabella_contingenza.columns.map({0:'Deceduti',1:'Sopravvissuti'})
        if column == 'Classe Passeggero':
            tabella_contingenza.columns = tabella_contingenza.columns.map({1: '1^ Classe', 2: '2^ Classe', 3: '3^ Classe'})
        else:
            tabella_contingenza.columns = tabella_contingenza.columns.map({0:'Femmine',1:'Maschi'})
        print(f'TABELLA DI CONTINGENZA {column} - {target}: ', tabella_contingenza, sep='\n')

        chi2, p, dof, expected = chi2_contingency(tabella_contingenza)
        print(f'Il p-value risultante dal test chi quadro sulla tabella di contingenza {column} - {target} è: {p}')
        print(f'Notazione non scientifica del p-value: {format(p, '.53f')}') #limite massimo decimali

        cramer = contingency.association(tabella_contingenza, method='cramer')

        print(f'L\'indice di Cramer calcolato sulla tabella di contingenza {column} - {target} è pari a: {cramer}')

        return tabella_contingenza

modello = ModelloReddito(_DATASET_PATH)
#modello.analisi_generali(modello.dataframe_sistemato)
#modello.dataframe_sistemato.to_csv(_DATASET_PATH_FIXED, index = False)
#modello.analisi_valori_univoci(modello.dataframe_sistemato)