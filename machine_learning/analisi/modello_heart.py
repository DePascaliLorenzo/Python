from modello_base import ModelloBase
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA

_DATASET_PATH = '../dataset/data_07.csv'

class ModelloHeart(ModelloBase):

    # metodo di inizializzazione
    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.variabili_quantitative, self.variabili_categoriali, self.scaler, self.encoder, self.dataframe_sistemato = self.sistemazione_dataframe()
        self.pca, self.dataframe_ridotto = self.riduzione_dataframe()

    # metodo di sistemazione del dataframe
    def sistemazione_dataframe(self):
        # separazione tra variabili quantitative e categoriali
        variabili_quantitive = ['age','trestbps','chol','thalach','oldpeak','ca']
        variabili_categoriali = ['sex','cp','fbs','restecg','exang','slope','thal']
        # standardizzazione delle sole variabili quantitative
        scaler = StandardScaler()
        df_quantitative = pd.DataFrame(scaler.fit_transform(self.dataframe[variabili_quantitive]), columns = variabili_quantitive)

        # one-hot-encoding delle sole variabili categoriali
        encoder = OneHotEncoder(sparse_output=False) # sparse_output=False serve per ottenere un array invece di una matrice sparsa da convertire
        df_categoriali = pd.DataFrame(encoder.fit_transform(self.dataframe[variabili_categoriali]))
        df_categoriali.columns = encoder.get_feature_names_out(variabili_categoriali) # aggiornamento nomi colonne
        # riunificazione in un nuovo dataframe
        df_sistemato = pd.concat([df_quantitative,df_categoriali], axis = 1)
        # return di vari elementi per il loro utilizzo
        return variabili_quantitive, variabili_categoriali, scaler, encoder, df_sistemato

    # metodo di riduzione della dimensionalità dataframe
    def riduzione_dataframe(self):
        pca = PCA(n_components=2)
        df_ridotto = pd.DataFrame(pca.fit_transform(self.dataframe_sistemato),columns = ['PC1','PC2'])
        return pca, df_ridotto

# utilizzo modello
modello = ModelloHeart(_DATASET_PATH)
modello.analisi_generali(modello.dataframe_ridotto)
# modello.analisi_valori_univoci(modello.dataframe, ['age','trestbps','chol','thalach','oldpeak'])
# modello.analisi_indici_statistici(modello.dataframe)
# modello.individuazione_outliers(modello.dataframe,['sex','cp','fbs','restecg','exang','slope','thal'])
# se gli outliers superano il 10% cominciano a dare fastidio al dataset e si fa solo per le quantitative