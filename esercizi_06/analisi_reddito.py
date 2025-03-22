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
label_new = ['Età', 'Categoria di Lavoro','Peso Campionario','Educazione','Anni di Studio','Stato Coniugale','Mansione','Relazione','Razza','Sesso','Entrate','Uscite','Ore Settimanali','Paese d\'Origine','Obiettivo']
drop_list_old = [label_old[2], label_old[4], label_old[14]]
drop_list_new = [label_new[2], label_new[4], label_new[14]]
native_countries_list = ['?', 'United-States', 'Cuba', 'Jamaica', 'India', 'Mexico', 'South', 'Puerto-Rico', 'Honduras',
                         'England', 'Canada', 'Germany', 'Iran', 'Philippines', 'Italy', 'Poland', 'Columbia', 'Cambodia',
                         'Thailand', 'Ecuador', 'Laos', 'Taiwan', 'Haiti', 'Portugal', 'Dominican-Republic', 'El-Salvador',
                         'France', 'Guatemala', 'China', 'Japan', 'Yugoslavia', 'Peru', 'Outlying-US(Guam-USVI-etc)',
                         'Scotland', 'Trinadad&Tobago', 'Greece', 'Nicaragua', 'Vietnam', 'Hong', 'Ireland', 'Hungary',
                         'Holand-Netherlands']

class ModelloReddito(ModelloBase):

    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.dataframe_sistemato = self.sistemazione_dataframe()
        # self.contingenza_classe = self.tabella_contingenza('Classe Passeggero', 'Sopravvissuto')
        #self.contingenza_genere = self.tabella_contingenza('Genere', 'Sopravvissuto')
        # self.correlazione_spearman('Età','Sopravvissuto')
        # self.grafici_contingenza()
        # self.grafico_spearman()
        # self.grafico_ripartizione()

    def sistemazione_dataframe(self):

        df_sistemato = self.dataframe.drop(drop_list_old, axis = 1)

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

        return df_sistemato
        """
        df_sistemato[label_new[13]] = df_sistemato[label_new[13]].map({'?':0, 'United-States':1, 'Cuba':2, 'Jamaica':3, 'India':4, 'Mexico':5, 'South':6, 'Puerto-Rico':7, 'Honduras':8, 'England':9,
'Canada':10, 'Germany':11, 'Iran':12, 'Philippines':13, 'Italy':14, 'Poland':15, 'Columbia':16, 'Cambodia':17, 'Thailand':18, 'Ecuador':19,
'Laos':20, 'Taiwan':21, 'Haiti':22, 'Portugal':23, 'Dominican-Republic':24, 'El-Salvador':25, 'France':26, 'Guatemala':27, 'China':28, 'Japan':29,
'Yugoslavia':30, 'Peru':31, 'Outlying-US(Guam-USVI-etc)':32, 'Scotland':33, 'Trinadad&Tobago':34, 'Greece':35, 'Nicaragua':36, 'Vietnam':37, 'Hong':38,
'Ireland':39, 'Hungary':40, 'Holand-Netherlands':41})
        """

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
modello.analisi_generali(modello.dataframe_sistemato)
modello.dataframe_sistemato.to_csv(_DATASET_PATH_FIXED, index = False)
modello.analisi_valori_univoci(modello.dataframe_sistemato)