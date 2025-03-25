from sklearn.preprocessing import StandardScaler

from machine_learning.analisi.modello_base import ModelloBase
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score,classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

_DATASET_PATH = '../dataset/data_06.csv'

class ModelloIris(ModelloBase):

    # metodo di inizializzazione
    def __init__(self,dataset_path):
        self.df = pd.read_csv(dataset_path)
        self.scaler, self.modello_classificazione = self.classificazione()

    # metodo per generazione modello di classificazione Perceptron
    def classificazione(self):
        # suddivisione dataframe in variabili e target (no biimensionale)
        y = self.df['class'] # target
        x = self.df.drop(columns = ['class'], axis = 1) # variabili
        # suddivisione delle osservazioni in addestramento (70%) e test (30%)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)
        # standardizzazione dei valori delle variabili
        scaler = StandardScaler()
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.transform(x_test)


        # creazione e addestramento del modello di classificazione
        classificazione = Perceptron()
        classificazione.fit(x_train,y_train)
        # predizioni del modello
        predizione = classificazione.predict(x_test)
        # valutazione del modello
        print('***** VALUTAZIONE MODELLO CLASSIFICAZIONE *****')
        print(f'L\'accuratezza della predizione del modello è pari a: {accuracy_score(y_test, predizione)}')
            # l'accuratezza è considerabile buona solo se sopra il 90%
        print('Il report di classificazione del modello è pari a:', classification_report(y_test,predizione), sep = '\n')
        # matrice predizioni del modello
        matrice_predizioni = confusion_matrix(y_test,predizione)
        print('***** MATRICE PREDIZIONI *****', matrice_predizioni, sep='\n')
        # generazione heatmap matrice predizioni
        plt.figure(figsize = (8,6))
        sns.heatmap(matrice_predizioni, annot = True, fmt = 'd', cmap = 'inferno', xticklabels = classificazione.classes_, yticklabels= classificazione.classes_)
        plt.title('Matrice Predizioni')
        plt.xlabel('Classi Predette', fontsize = 12)
        plt.ylabel('Classi Reali', fontsize = 12)
        plt.show()
        # generazione grafico di distribuzione predizioni
        self.grafico_predizioni(matrice_predizioni)
        return scaler, classificazione

    # metodo per generare un grafico delle predizioni
    @staticmethod
    def grafico_predizioni(matrice_predizioni):
        plt.bar([0, 1.4, 2.8], matrice_predizioni[:,0], width = 0.4, label= 'setosa', color = 'blue')
        plt.bar([0, 1.8, 3.2], matrice_predizioni[:, 1], width=0.4, label='versicolor', color='green')
        plt.bar([0.8, 2.2, 3.6], matrice_predizioni[:, 2], width=0.4, label='virginica', color='red')
        plt.xticks([0,1.8,3.6], ['setosa','versicolor','virginica'])
        plt.xlabel('Specie')
        plt.ylabel('Numero di Predizioni')
        plt.legend()
        plt.show()

    # metodo per esportazione su file modello e scaler
    def esportazione(self):
        joblib.dump(self.modello_classificazione, '../modelli/modello_iris.joblib')
        joblib.dump(self.scaler,'../modelli/scaler_iris.joblib')


# utilizzo modello
modello = ModelloIris(_DATASET_PATH)
# modello.analisi_generali(modello.df)
# modello.analisi_valori_univoci(modello.df, ["sepal_length", "sepal_width", "petal_length", "petal_width"])
# modello.analisi_indici_statistici(modello.df)
# modello.individuazione_outliers(modello.df, ['class'])
modello.esportazione()