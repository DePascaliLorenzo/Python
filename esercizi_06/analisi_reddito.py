# Analizza il dataset "people.csv" allegato per individuare
# la correlazione più significativa tra le variabili presenti e la variabile target.
# L'obiettivo finale consiste nell'ottenimento dei dati di correlazione e del relativo grafico.
from machine_learning.analisi.modello_base import ModelloBase
import pandas as pd
from scipy.stats import chi2_contingency,contingency,spearmanr
import matplotlib.pyplot as plt

_DATASET_PATH = '06. people.csv'
label_old = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','target']
label_new = ['Età', 'Categoria di Lavoro','Peso Campionario','Educazione','Anni di Studio','Stato Coniugale','Mansione','Relazione','Razza','Sesso','Entrate','Uscite','Ore Settimanali','Paese d\'Origine','Obiettivo']
drop_list_old = [label_old[2], label_old[4], label_old[14]]
drop_list_new = [label_new[2], label_new[4], label_new[14]]

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
modello.analisi_valori_univoci(modello.dataframe_sistemato)