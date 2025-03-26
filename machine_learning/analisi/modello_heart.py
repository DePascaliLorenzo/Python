from scipy.cluster.vq import kmeans
from scipy.stats import alpha

from modello_base import ModelloBase
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA
from kneed import KneeLocator
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns

_DATASET_PATH = '../dataset/data_07.csv'

class ModelloHeart(ModelloBase):

    # metodo di inizializzazione
    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        self.variabili_quantitative, self.variabili_categoriali, self.scaler, self.encoder, self.dataframe_sistemato = self.sistemazione_dataframe()
        self.pca, self.dataframe_ridotto = self.riduzione_dataframe()
        self.numero_cluster = self.individuazione_cluster()
        self.livelli_rischio ={0: 'Basso', 1:'Medio', 2: 'Alto'}
        self.modello_clustering = self.clustering()
        self.grafico_cluster()

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

    # metodo per individuazione numero ottimale cluster
    def individuazione_cluster(self):
        inertia = []
        cluster_range = range(1,11)
        for k in cluster_range:
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(self.dataframe_ridotto)
            inertia.append(kmeans.inertia_)
        # analisi numero ottimale cluster con strumento automatico
        knee_locator = KneeLocator(cluster_range, inertia, curve = 'convex', direction='decreasing')
        numero_ottimale_cluster = knee_locator.knee
        print(f'Numero ottimale cluster rilevato da KneeLocator: {numero_ottimale_cluster}')
        # conferma del numero ottimale del cluster mediante "grafico a ginocchio"
        plt.figure(figsize=(10,6))
        plt.plot(cluster_range,inertia, marker = 'o')
        plt.xlabel('Numero Cluster')
        plt.ylabel('Inertia')
        plt.title('Metodo Elbow per selezione numero ottimale cluster')
        plt.show()

        return numero_ottimale_cluster

    # metodo per il clustering delle nostre osservazioni
    def clustering(self):
        # creazione e addestramento del modello (aggiunta al dataframe di una nuova colonna con n° del cluster assegnato)
        kmeans = KMeans(n_clusters=self.numero_cluster, random_state=42)
        self.dataframe_ridotto['Cluster'] = kmeans.fit_predict(self.dataframe_ridotto)
        # aggiunta nuova colonna al dataframe per sostituzione n° cluster con etichetta testuale
        self.dataframe_ridotto['Rischio'] = self.dataframe_ridotto['Cluster'].map(self.livelli_rischio)
        # conversione colonna Rischio in una colonna di tipo categorico ordinato
        ordine_rischio = [self.livelli_rischio[key] for key in sorted(self.livelli_rischio.keys())]
        self.dataframe_ridotto['Rischio'] = pd.Categorical(self.dataframe_ridotto['Rischio'], categories = ordine_rischio, ordered=True)

        return kmeans

    # metodo per visualizzazione dei cluster in un grafico
    def grafico_cluster(self, paziente = None):
        plt.figure(figsize=(14,10))
        # visualizzazione osservazioni
        sns.scatterplot(data=self.dataframe_ridotto,x = 'PC1', y = 'PC2', hue = 'Rischio', palette='viridis', style='Rischio', s = 100, alpha = 0.7)
        # visualizzazione centroidi
        centroidi = self.modello_clustering.cluster_centers_
        plt.scatter(centroidi[:,0], centroidi[:,1], c='black',marker = 'o', s = 300, label = 'Centroidi')
        # visualizzazione nuovo paziente se esiste
        if not paziente is None:
            plt.scatter(paziente['PC1'], paziente['PC2'], c = 'red', s=200, marker = 'X', label = 'Nuovo Paziente')
        # indicazioni testuali
        plt.title('Distribuzione pazienti per livelli di rischio cardiaco')
        plt.xlabel('PC1')
        plt.ylabel('PC2')
        plt.legend(title = 'Livelli di Rischio')
        plt.show()

    # la distanza tra i centroidi indica la bontà del modello, più sono lontani, meglio è

    # metodo per la valutazione livello di rischio di un nuovo paziente
    def valutazione_paziente(self, dati_paziente):
        # costruzione dataframe per il nuovo paziente
        df_paziente = pd.DataFrame([dati_paziente]) # singola osservazione
        # standardizzazione variabili quantitative
        df_paziente_quant = pd.DataFrame(self.scaler.transform(df_paziente[self.variabili_quantitative]), columns=self.variabili_quantitative)
        # one-hot-encoding variabili categoriali
        df_paziente_cat = pd.DataFrame(self.encoder.transform(df_paziente[self.variabili_categoriali]))
        df_paziente_cat.columns = self.encoder.get_feature_names_out(self.variabili_categoriali)
        # riunificazione dataframe
        df_paziente_sistemato = pd.concat([df_paziente_quant,df_paziente_cat], axis = 1)
        # riduzione dimensionale
        df_paziente_ridotto = pd.DataFrame(self.pca.transform(df_paziente_sistemato), columns = ['PC1','PC2'])
        # predizione del cluster
        cluster = self.modello_clustering.predict(df_paziente_ridotto)[0]
        livello_rischio = self.livelli_rischio[cluster]
        print(f'Livelli Rischio Paziente: {livello_rischio}')
        # invocazione metodo per visualizzazione nel grafico
        self.grafico_cluster(df_paziente_ridotto)




# utilizzo modello
modello = ModelloHeart(_DATASET_PATH)
# modello.analisi_generali(modello.dataframe_ridotto)
# modello.analisi_valori_univoci(modello.dataframe, ['age','trestbps','chol','thalach','oldpeak'])
# modello.analisi_indici_statistici(modello.dataframe)
# modello.individuazione_outliers(modello.dataframe,['sex','cp','fbs','restecg','exang','slope','thal'])
# se gli outliers superano il 10% cominciano a dare fastidio al dataset e si fa solo per le quantitative

# predizione nuovo paziente
nuovo_paziente = {
    "age": 55,
    "sex": 1,
    "cp": 2,
    "trestbps": 130,
    "chol": 250,
    "fbs": 0,
    "restecg": 1,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 1.5,
    "slope": 1,
    "ca": 0,
    "thal": 2
}
modello.valutazione_paziente(nuovo_paziente)