import pandas as pd

# funzione per ottenimento informazioni generali
def analisi_generale(df):
    print('Dataframe Completo', df.to_string(), sep = '\n')
    print('Prime cinque osservazioni: ', df.head().to_string(), sep = '\n')
    print('Ultime cinque osservazioni: ', df.tail().to_string(), sep = '\n')
    print('Informazioni generali dataframe:')
    df.info()

#funzione per analisi delle singole colonne (variabili)
def scomposizione_dataframe_colonne(df):
    print('Scomposizione in Colonne')
    for colonna in df.columns:
        print(f'Colonna {colonna}:', df[colonna], type(df[colonna]), sep = '\n')
        print('Valori Colonna')
        for valore in df[colonna]:
            print(valore, type(valore))

# funzione per analisi delle singole righe (osservazioni)
def scomposizione_dataframe_righe(df):
    print('Scomposizione in righe')
    for index, obs in df.iterrows():
        print(f'Riga {index}', obs, type(obs), sep = '\n')
        print('Valori Riga: ')
        for valore in obs:
            print(valore, type(valore))

# funzione per filtro dataframe su colonne
def filtro_dataframe_colonne(df):
    df_filtrato_colonne = df[['Reddito_annuo', 'Soddisfazione']]
    print(df_filtrato_colonne.to_string())

# funzione per filtro dataframe su colonne
def filtro_dataframe_osservazione(df):
    valori = ['Laurea triennale','Laurea magistrale']
    df_filtrato_osservazioni = df[df['Titolo di studio'].isin(valori)]
    print(df_filtrato_osservazioni.to_string())

# funzione per controllo valori univoci variabili categoriali
def analisi_valori_univoci(df):
    df_categoriali = df.drop(['Età', 'Reddito_annuo', 'Spese_mensili'], axis = 1) # axis 0 per drop categoriale, 1 per drop varibili
    for col in df_categoriali.columns:
        print(f'In colonna {col} abbiamo: {df_categoriali[col].nunique()} valori univoci')
        for value in df_categoriali[col].unique():
            print(value)

# funzione per analisi indici statistici variabili quantitative
def analisi_indici_statistici(df):
    # indici generali variabili quantitative del df
    indici_generali = df.describe()
    print('Indici statistici generali variabili quantitative: ',indici_generali, sep = '\n')
    # estrazione variabili quantitative
    df_quantitative = df.drop(['Soddisfazione', 'Stato_civile', 'Titolo di studio'], axis = 1)
    # deviazione standard su popolazione
    for col in df_quantitative.columns:
        deviazione_standard_popolazione = df_quantitative[col].std(ddof = 0)
        print(f'Deviazione standard popolazione colonna {col}: {deviazione_standard_popolazione}')

# generazione dataframe da file csv
dataframe = pd.read_csv('../dataset/data_03.csv')

# invocazione funzioni
# analisi_generale(dataframe)
# scomposizione_dataframe_colonne(dataframe)
# scomposizione_dataframe_righe(dataframe)
# filtro_dataframe_colonne(dataframe)
# filtro_dataframe_osservazione(dataframe)
# analisi_valori_univoci(dataframe)
analisi_indici_statistici(dataframe)