from modello_base import ModelloBase
import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np
import matplotlib.pyplot as plt

class ModelloAlcolici(ModelloBase):

    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.dataframe_sistemato = self.sistemazione_dataframe()
        self.tabella_contingenza('AGE')
        self.tabella_contingenza('SEX')

    def sistemazione_dataframe(self):

        # 1. copia dataframe
        df_sistemato = self.dataframe.copy()

        # 2. drop colonne completamente prive di valori
        df_sistemato = df_sistemato.dropna(axis = 1, how = 'all')

        # 3. drop colonne con valore unico
        colonne_unico_valore = []
        for col in df_sistemato.columns:
            if df_sistemato[col].nunique() < 2:
                colonne_unico_valore.append(col)
        df_sistemato = df_sistemato.drop(colonne_unico_valore, axis = 1)

        # 4. eliminazione righe con valori MEASURE = HSC - SEX = 9 - AGE = Y_GE11
        indici_righe_da_eliminare = df_sistemato.index[(df_sistemato['MEASURE'] == 'HSC') | (df_sistemato['SEX'] == 9) | (df_sistemato['AGE'] == 'Y_GE11')]
        df_sistemato = df_sistemato.drop(indici_righe_da_eliminare, axis = 0)

        return df_sistemato

    # metodo per ottenere tabelle di contingenza - test chi-quadro - indici Cramer
    def tabella_contingenza(self, column):

        # generazione e stampa tabella contingenza
        tabella_contingenza = pd.crosstab(self.dataframe_sistemato[column],
                                          self.dataframe_sistemato['DATA_TYPE'],
                                          values = self.dataframe_sistemato['OBS_VALUE'],
                                          aggfunc = 'sum')

        # sostituzione label tabella di contingenza
        tabella_contingenza.columns = tabella_contingenza.columns.map({'11_ALCF_1VOL': 'Cons_Alc_F_Pasto -1/Settimana',
                                                                       '11_ALC_FUORI': 'Cons_Alc_F_Pasto',
                                                                       '11_ALC_NFUORI' : 'No_Cons_Alc_F_Pasto'})
        if column == 'SEX':
            tabella_contingenza.index = tabella_contingenza.index.map({1: 'Maschi',2:'Femmine'})

        # stampa tabella contingenza
        print(f'***** TABELLA CONTINGENZA {column} - DATA_TYPE', tabella_contingenza.to_string(), sep='\n')

        # test del chi-quadro e stampa esito (p-value)
        chi2, p, dof, expected = chi2_contingency(tabella_contingenza)
        print(f'Il p-value risultante da test del chi-quadro tra {column} - DATA_TYPE è {format(p, '.53f')}')

        # calcolo dell'indice di Cramer e stampa esito
        totale_osservazioni = tabella_contingenza.sum().sum() # .sum().sum() somma tutti i values sia per righe che per colonne
        # in questo caso, è la somma di tutti gli OBS_VALUE
        print(totale_osservazioni, type(totale_osservazioni))
        dimensione_minima = min(tabella_contingenza.shape) - 1 # valore minimo in una tupla righe-colonne tabella contingenza
        cramer = np.sqrt(chi2 / (totale_osservazioni * dimensione_minima))
        print(f'L\'indice di Cramer calcolato sulla tabella di contingenza {column} - DATA_TYPE è: ', cramer) # invocazione metodo per generazione grafico
        self.grafico_contingenza(tabella_contingenza, "Fascia Età" if column == "AGE" else "Genere")

    # metodo per generazione grafici di distribuzione a barre
    def grafico_contingenza(self, tabella_contingenza, colonna):
        tabella_contingenza.plot(kind="bar", stacked=True, color=["yellow", "red", "green"])
        plt.title(f"Frequenza di Consumo per {colonna}")
        plt.xlabel(colonna)
        plt.ylabel("Persone")
        plt.legend()
        plt.tick_params(rotation=45, axis="x")
        plt.tight_layout()
        plt.show()

# utilizzo modello
modello = ModelloAlcolici('../dataset/data_08.csv')
# modello.analisi_generali(modello.dataframe_sistemato)
# modello.analisi_valori_univoci(modello.dataframe_sistemato)