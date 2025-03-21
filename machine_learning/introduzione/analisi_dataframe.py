import pandas as pd
import matplotlib.pyplot as plt

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
    # moda variabili quantitative e categoriali
    for col in df.columns:
        print(f'Moda colonna {col}: ', df[col].mode().iloc[0])
    # invocazione funzione per individuazione outliers
    print('----- INDIVIDUAZIONE OUTLIERS -----')
    for col in df_quantitative.columns:
        individuazione_outliers(df_quantitative, col)

# funzione per individuazione outliers nelle variabili quantitative
def individuazione_outliers(df, colonna):
    # calcolo differenza interquartile
    q1 = df[colonna].quantile(0.25)
    q3 = df[colonna].quantile(0.75)
    iqr = q3 - q1 # iqr sta per 'Differenza interquartile'
    # calcolo limiti inferiore/superiore outliers
    limite_inferiore = q1 - 1.5 * iqr
    limite_superiore = q3 + 1.5* iqr
    # individuazione outliers
    outliers = df[(df[colonna] < limite_inferiore) | (df[colonna] > limite_superiore)]
    print(f'Nella colonna {colonna} sono presenti n° {len(outliers)} ({len(outliers) / len(df) * 100}%)')
    if colonna == 'Spese_mensili':
        generazione_diagramma_indici(df,colonna, limite_superiore, limite_inferiore)

# funzione per generare un diagramma a scatola degli indici delle variabili quantitative
def generazione_diagramma_indici(df, colonna, limite_superiore, limite_inferiore):
    # calcolo indici generali colonna
    indici_colonna = df[colonna].describe()
    # generazione grafico
    plt.boxplot(df[colonna])

    # reppresentazione quartili
    plt.text(x = 1.08, y = indici_colonna['75%'], s = f'Terzo Quartile {indici_colonna['75%']}', color = 'b', fontsize = 9) # x e y rappresentano la distanza della scritta dal grafico
    plt.text(x=1.08, y=indici_colonna['50%'], s=f'Mediana {indici_colonna['50%']}', color='r',
             fontsize=9)  # x e y rappresentano la distanza della scritta dal grafico
    plt.text(x=1.08, y=indici_colonna['25%'], s=f'Primo Quartile {indici_colonna['25%']}', color='m',
             fontsize=9)  # x e y rappresentano la distanza della scritta dal grafico

    # rappresentazione massimo e minimio
    plt.text(x=1.08, y=indici_colonna['max'], s=f'Massimo Rilevato {indici_colonna['max']}', color='g',
             fontsize=9)  # x e y rappresentano la distanza della scritta dal grafico
    plt.text(x=1.08, y=indici_colonna['min'], s=f'Minimo Rilevato {indici_colonna['min']}', color='y',
             fontsize=9)  # x e y rappresentano la distanza della scritta dal grafico

    # rappresentazione limiti outliers
    plt.axhline(y = limite_superiore, color = 'r', linestyle = '--', linewidth = 3)
    plt.text(x=1.08, y=limite_superiore + 300, s=f'Soglia Outlier Superiore {limite_superiore}', color='r',
             fontsize=10)  # x e y rappresentano la distanza della scritta dal grafico
    plt.axhline(y=limite_inferiore, color='r', linestyle='--', linewidth=3)
    plt.text(x=1.08, y=limite_inferiore + 300, s=f'Soglia Outlier Inferiore {limite_inferiore}', color='r',
             fontsize=10)  # x e y rappresentano la distanza della scritta dal grafico

    plt.show()

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