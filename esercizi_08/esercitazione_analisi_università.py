"""
Si richiede il compimento di un’indagine statistica per capire se vi siano legami tra facoltà universitarie, qualifiche
dei docenti e loro genere sulla base dei dati reperibili al seguente link
Dopo aver compiuto un’analisi esplorativa dei dati ricercati, determinare una possibile correlazione tra:
le facoltà universitarie e le qualifiche dei docenti (ordinario, associato, ricercatore)
le facoltà universitarie e il genere dei docenti (uomo, donna)
Si richiede la produzione in output dei risultati di correlazione e dei relativi grafici esplorativi.
"""
from scipy.stats import chi2_contingency, contingency

from machine_learning.analisi.modello_base import ModelloBase
import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

class ModelloDocenti(ModelloBase):

    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.dataframe_pulito = self.pulizia_dataframe()
        self.tabella_contingenza('Qualifica')
        self.tabella_contingenza('Genere')

    def pulizia_dataframe(self):
        df_pulito = self.dataframe.copy()
        df_pulito = df_pulito.dropna(axis = 1, how = 'all')
        colonne_unico_valore = []
        for col in df_pulito.columns:
            if df_pulito[col].nunique() < 2:
                colonne_unico_valore.append(col)
        df_pulito = df_pulito.drop(colonne_unico_valore, axis = 1)
        df_pulito = df_pulito.drop(['TIME_PERIOD'], axis = 1)
        indici_righe_eliminare = df_pulito.index[(df_pulito['SEX'] == 9) | (df_pulito['FACULTY_TYPE'] == 99) | (df_pulito['TYPE_UNIV_MANAGEMENT'] == 9) | (df_pulito['TITLE'] == 9)]
        df_pulito = df_pulito.drop(indici_righe_eliminare, axis = 0)
        df_pulito = df_pulito.rename(columns = {'TYPE_UNIV_MANAGEMENT': 'Tipo Università', 'FACULTY_TYPE':'Facoltà', 'SEX': 'Genere', 'TITLE': 'Qualifica', 'OBS_VALUE': 'Valore Osservazioni'})
        return df_pulito

    def tabella_contingenza(self, col):
        tabella_contingenza = pd.crosstab(self.dataframe_pulito[col], self.dataframe_pulito['Facoltà'], values=self.dataframe_pulito['Valore Osservazioni'], aggfunc='sum')
        tabella_contingenza.columns = tabella_contingenza.columns.map({
            1: "Agraria", 2: "Architettura", 3: "Chimica Industriale", 4: "Conservazione Beni Culturali",
            5: "Economia", 6: "Farmacia", 7: "Giurisprudenza", 8: "Ingegneria", 9: "Lettere e Filosofia",
            10: "Lingue e Letterature Straniere", 11: "Medicina e Chirurgia", 12: "Medicina Veterinaria",
            13: "Psicologia", 14: "Scienze Ambientali", 15: "Scienze della Formazione",
            16: "Scienze Matematiche, Fisiche e Naturali", 17: "Scienze Motorie", 18: "Scienze Politiche",
            19: "Scienze Statistiche", 20: "Sociologia", 21: "Altro"})
        if col == 'Qualifica':
            tabella_contingenza.index = tabella_contingenza.index.map({
                1: 'Professore Ordinario', 2: 'Professore Associato', 3: 'Ricercatore'
            })
        else:
            tabella_contingenza.index = tabella_contingenza.index.map({
                1: 'Maschi', 2: 'Femmine'
            })
        print(f'***** TABELLA CONTINGENZA {col} - Facoltà *****', tabella_contingenza.transpose().to_string(), sep = '\n')
        chi2, p, dof, expected = chi2_contingency(tabella_contingenza)
        print(f'***** TEST CHI-QUADRO {col} - Facoltà *****', f'Chi-quadro: {chi2}', f'p-value: {format(p,'.53f')}', sep='\n')
        cramer = contingency.association(tabella_contingenza, method='cramer')
        print(f'***** INDICE CRAMER {col} - Facoltà *****',f'L\'indice di Cramer è: {cramer}', sep='\n')
        self.grafico_contingenza(tabella_contingenza,col)
        return tabella_contingenza

    @staticmethod
    def grafico_contingenza(tabella_contingenza, col):
        tabella_contingenza.transpose().plot(kind='bar')
        plt.title('Tipo Qualifica - Facoltà')
        plt.xlabel(col)
        plt.ylabel('Valore Osservato')
        plt.legend(title = col, loc = 'upper left')
        plt.tick_params(rotation = 90, axis = 'x', labelsize = 6)
        plt.tight_layout()
        plt.show()

modello = ModelloDocenti('Docenti.csv')
# modello.analisi_generali(modello.dataframe_pulito)
# modello.analisi_valori_univoci(modello.dataframe_pulito)