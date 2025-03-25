import joblib
import pandas as pd

# dichiarazione di un nuovo fiore
nuovo_fiore = {
    'sepal_length': 5.8,
    'sepal_width': 2.7,
    'petal_length': 4.1,
    'petal_width': 1.0
}

# conversione del dizionario in Dataframe tramite pandas
df_nuovo_fiore = pd.DataFrame([nuovo_fiore]) # parentesi quadra in quanto unica osservazione

# recupero modello predittico e scaler dai file
modello_predittivo = joblib.load('modello_iris.joblib')
scaler_modello = joblib.load('scaler_iris.joblib')

# standardizzazione dei nuovi dati e predizione
df_nuovo_fiore_std = scaler_modello.transform(df_nuovo_fiore)
print(f'Classe Predetta: {modello_predittivo.predict(df_nuovo_fiore_std)[0]}')