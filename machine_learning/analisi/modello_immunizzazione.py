from modello_base import ModelloBase
import pandas as pd
import pycountry
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class ModelloImmunizzazione(ModelloBase):

    def __init__(self,dataset_path):
        self.dataframe = pd.read_csv(dataset_path, skiprows=4)
        # skiprows= 4 salta le prime 4 righe, che impediscono la lettura corretta del .csv
        self.dataframe_sistemato = self.sistemazione_dataframe()

    def sistemazione_dataframe(self):
        # 1. drop di colonne con valori duplicati o prive di valori
        df_sistemato = self.dataframe.copy().drop(['Country Code','Indicator Code','Unnamed: 68'], axis = 1)
        # 2. filtro per indicatori di interesse (operazione avvenuta dopo averli trovati col metodo di individuazione)
        indicatori_interesse = [
            'Mortality rate, under-5 (per 1,000 live births)',
            'Immunization, measles (% of children ages 12-23 months)',
            'Immunization, DPT (% of children ages 12-23 months)',
            'Immunization, HepB3 (% of one-year-old children)'
        ]
        df_sistemato = df_sistemato[df_sistemato['Indicator Name'].isin(indicatori_interesse)]
        # 3. rimozione osservazioni completamente prive di valori in tutte le colonne anni
        anni = [str(anno) for anno in range(1960,2024)]
        df_sistemato = df_sistemato.dropna(subset = anni, how = 'all')
        # 4. sostituzione valori nan in colonna anni con 0 (calori mancanti)
        df_sistemato[anni] = df_sistemato[anni].fillna(0)
        # 5. sostituzione colonne anni con un'unica colonna totale anni
        df_sistemato['Total Value (1960-2023)'] = df_sistemato.iloc[:, 2:].sum(axis = 1)
        df_sistemato = df_sistemato.drop(columns = anni, axis = 1)
        # 6. conversione del datafram da formato lungo a formato largo
        df_sistemato = df_sistemato.pivot_table(
            index = 'Country Name',
            columns = 'Indicator Name',
            values = 'Total Value (1960-2023)',
            fill_value = 0 # per riempire possibile valori non derivanti da ristrutturazione del dataframe
        ).reset_index()
        df_sistemato.columns.name = None # da fare per non avere Indicator Name come intestazioni indici di riga
        # 7. aggiunta colonna immunizzazione con totale valori delle varie immunizzazioni
        df_sistemato['Immunization (%)'] = df_sistemato.iloc[:, 1:4].sum(axis = 1)
        # 8. esclusione regioni di aggregazione
        lista_paesi_ufficiali = [country.name for country in pycountry.countries]
        df_sistemato = df_sistemato[df_sistemato['Country Name'].isin(lista_paesi_ufficiali)]
        # 9. aggiunta colonna mortalità con valori espressi in precentuale
        df_sistemato['Mortality rate, under-5 (%)'] = df_sistemato['Mortality rate, under-5 (per 1,000 live births)'] / 10

        return df_sistemato

    # metodo per individuazione indicatori di interesse
    def individuazione_indicatori(self):
        parole_chiave = ['Mortality', 'Immunization']
        valori_unici_filtrati = [value for value in self.dataframe_sistemato['Indicator Name'].unique() if any(parola in value for parola in parole_chiave)]
        for valore in valori_unici_filtrati:
            print(valore)

    # metodo per correlazione e regressione lineare semplice immunizzazione (regressore) e mortalità (target)
    def correlazione_regressione(self):
        # analisi correlazione
        corr, p = pearsonr(self.dataframe_sistemato['Immunization (%)'],
                           self.dataframe_sistemato['Mortality rate, under-5 (%)'])
        print(f'La correlazione di Pearson risultante tra Immunizzazione e Mortalità Infantile è: {corr}')
        print(f'Il p-value sulla correlazione tra Immunizzazione e Mortalità Infantile è: {p}')
        # definizione variabile target e regressore
        y = self.dataframe_sistemato[['Mortality rate, under-5 (%)']].values.reshape(-1,1) # target
        x = self.dataframe_sistemato[['Immunization (%)']].values.reshape(-1,1) #regressore
        # creazione e addestramento semplificato modello
        regressione = LinearRegression()
        regressione.fit(x,y)
        # ottenimento della retta di regressione
        retta_regressione = regressione.predict(x)
        # grafico modello
        plt.scatter(x, y, s=3, color = 'blue')
        plt.plot(x,retta_regressione,color = 'red', linewidth = 1.1)
        plt.title('Regressione tra Immunizzazione e Mortalità Infantile')
        plt.xlabel('Immunizzazione')
        plt.ylabel('Mortalità')
        plt.show()

# utilizzo modello
modello = ModelloImmunizzazione('../dataset/data_09.csv')
# modello.analisi_generali(modello.dataframe_sistemato)

# analisi selettiva valori univoci (per colonna)
colonne_no_univoci = []
for col in modello.dataframe_sistemato.columns:
    if col != 'Country Name':
        colonne_no_univoci.append(col)
# modello.analisi_valori_univoci(modello.dataframe_sistemato,colonne_no_univoci)
# modello.individuazione_indicatori()

modello.correlazione_regressione()