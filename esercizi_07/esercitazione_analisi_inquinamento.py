"""
Analizza il dataset “pollution.csv” allegato per individuare una possibile correlazione tra la densità della popolazione
e i livelli di inquinamento da NO₂ e SO₂, con un focus sulle regioni con qualità dell’aria “moderata” e “scarsa”.
"""
from machine_learning.analisi.modello_base import ModelloBase
import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

_DATASET_PATH = 'dataset/pollution.csv'

class ModelloInquinamento(ModelloBase):

    def __init__(self):
        self.dataframe = pd.read_csv(_DATASET_PATH)
        self.dataframe_sistemato, self.scaler = self.sistemazione_dataframe()
        self.individuazione_correlazioni()
        self.regressione_lineare_semplice('NO2')
        self.regressione_lineare_semplice('SO2')

    def sistemazione_dataframe(self):
        df_sistemato = self.dataframe.copy()
        # index = len(dataframe_sistemato)
        # for i in range(index):
        #     if dataframe_sistemato.loc[i,'Air Quality'] == 'Hazardous':
        #         dataframe_sistemato.drop(index = i, axis = 0)
        df_sistemato = df_sistemato[df_sistemato['Air Quality'] != 'Hazardous']
        df_sistemato = df_sistemato[df_sistemato['Air Quality'] != 'Good']
        df_sistemato = df_sistemato[df_sistemato['SO2'] > 0]
        df_sistemato = df_sistemato.drop(['Air Quality'], axis = 1)
        col_da_std = df_sistemato.drop(['NO2','SO2'], axis = 1)
        scaler = StandardScaler()
        col_scalate = scaler.fit_transform(col_da_std)
        df_scalato = pd.DataFrame(col_scalate, columns = col_da_std.columns,index= df_sistemato.index)
        df_sistemato = pd.concat([df_scalato, df_sistemato['NO2'], df_sistemato['SO2']], axis = 1)
        return df_sistemato, scaler

    def individuazione_correlazioni(self):
        matrice = self.dataframe_sistemato.corr()
        print('***** MATRICE DI CORRELAZIONE *****', matrice.to_string(), sep = '\n')
        plt.figure(figsize=(10, 5))
        sns.heatmap(matrice, annot = True, cmap = 'coolwarm', fmt = '.2f', linewidth = 0.5)
        plt.xticks(rotation = 30, ha = 'right')
        plt.title('Heatmap delle Correlazioni')
        plt.show()

    # la 'target' NON VA MAI STANDARDIZZATA

    def regressione_lineare_semplice(self, target):
        y = self.dataframe_sistemato[[target]].values.reshape(-1,1)
        x = self.dataframe_sistemato[['Population_Density']].values.reshape(-1,1)
        regressione = LinearRegression()
        regressione.fit(x,y)
        retta_regressione = regressione.predict(x)
        print('***** PUNTEGGIO MODELLO REGRESSIONE *****', regressione.score(x,y), sep = '\n')
        col_index_pop = self.dataframe_sistemato.columns.get_loc('Population_Density')
        x_reali_pop = (x * self.scaler.scale_[col_index_pop]) + self.scaler.mean_[col_index_pop]
        plt.scatter(x_reali_pop, y, color = 'red', label= 'Osservazioni', linewidth = 1.5)
        plt.plot(x_reali_pop, retta_regressione, color = 'blue', label = 'Regressione Lineare', linewidth = 1.1)
        plt.title(f'Correlazione {target} - Population Density')
        plt.xlabel('Population Density')
        plt.ylabel(target)
        plt.show()

modello = ModelloInquinamento()
# modello.analisi_generali(modello.dataframe_sistemato)
# modello.analisi_valori_univoci(modello.dataframe_sistemato)
# modello.individuazione_outliers(modello.dataframe_sistemato, ['Air Quality'])