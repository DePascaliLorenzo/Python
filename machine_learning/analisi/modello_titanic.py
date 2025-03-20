from modello_base import  ModelloBase
import pandas as pd

class ModelloTitanic(ModelloBase):

    # metodo di inizializzazione
    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.dataframe_sistemato = self.sistemazione_dataframe()


    # metodo di istanza per sistemazione dataframe
    def sistemazione_dataframe(self):
        # 1. drop delle colonne inutili ai fine del modello
        variabili_da_droppare = ['name','ticket','fare','cabin','embarked','home.dest', 'boat', 'body']
        df_sistemato = self.dataframe.drop(variabili_da_droppare, axis=1)
        # 2. drop osservazione con tutti i valori nan
        df_sistemato = df_sistemato.drop(index = 1309, axis = 0)
        # 3. sostituzione valori nan colonna age con mediana
        # df_sistemato['age'] = df_sistemato['age'].fillna(df_sistemato['age'].median())
        df_sistemato['age'] = (df_sistemato.groupby(['pclass','sex'])['age']
                               .apply(lambda x: x.fillna(x.median())).reset_index(level=[0,1], drop = True))

        return df_sistemato

# utilizzo modello
modello = ModelloTitanic('../dataset/data_04.csv')
modello.analisi_generali(modello.dataframe_sistemato)
modello.analisi_valori_univoci(modello.dataframe_sistemato,
                               ['age','sibsp', 'parch'])
modello.individuazione_outliers(modello.dataframe_sistemato,'sex')