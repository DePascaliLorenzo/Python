import numpy as np
from modello_base import ModelloBase
import pandas as pd
from datetime import datetime

_DATASET_PATH = "../dataset/data_05.csv"

class ModelloHousing(ModelloBase):

    # meotodo di inizializzazione
    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.dataframe_sistemato = self.sistemazione_dataframe()

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
        return df_sistemato

# utilizzo modello
modello = ModelloHousing(_DATASET_PATH)
modello.analisi_generali(modello.dataframe_sistemato)
modello.analisi_indici_statistici(modello.dataframe_sistemato)
modello.individuazione_outliers(modello.dataframe_sistemato)