import matplotlib.pyplot as plt

from modello_base import  ModelloBase
import pandas as pd
from scipy.stats import chi2_contingency,contingency,spearmanr

class ModelloTitanic(ModelloBase):

    # metodo di inizializzazione
    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path)
        # self.dataframe_sistemato = self.sistemazione_dataframe()
        self.contingenza_classe = self.tabella_contingenza('Classe Passeggero', 'Sopravvissuto')
        self.contingenza_genere = self.tabella_contingenza('Genere', 'Sopravvissuto')
        self.correlazione_spearman('Età','Sopravvissuto')
        self.grafici_contingenza()
        self.grafico_spearman()
        self.grafico_ripartizione()


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
        # 4. rimappatura valori colonna sex (0: female - 1: malw)
        df_sistemato['sex'] = df_sistemato['sex'].map({'female':0, 'male': 1})
        # 5. modifica nomi colonne
        df_sistemato = df_sistemato.rename(columns = {
            'pclass' : 'Classe Passeggero',
            'survived' : 'Sopravvissuto',
            'sex' : 'Genere',
            'age' : 'Età',
            'sibsp' : 'Fratelli/Coniugi',
            'parch' : 'Genitori/Figli'
        })
        # 6. conversione tipo float in tipo int
        for col in df_sistemato:
            df_sistemato[col] = df_sistemato[col].astype(int)

        return df_sistemato

    # metodo per ottenere tabelle di contingenza - test chi quadro e Cramer (correlazione tra variabili categoriali)
    def tabella_contingenza(self,column, target):
        # generazione e stampa tabella di contingenza
        tabella_contingenza = pd.crosstab(self.dataframe[column], self.dataframe[target])

        tabella_contingenza.columns = tabella_contingenza.columns.map({0:'Deceduti',1:'Sopravvissuti'})
        if column == 'Classe Passeggero':
            tabella_contingenza.columns = tabella_contingenza.columns.map({1: '1^ Classe', 2: '2^ Classe', 3: '3^ Classe'})
        else:
            tabella_contingenza.columns = tabella_contingenza.columns.map({0:'Femmine',1:'Maschi'})
        print(f'TABELLA DI CONTINGENZA {column} - {target}: ', tabella_contingenza, sep='\n')
        # test chi quadro e stampa esito
        chi2, p, dof, expected = chi2_contingency(tabella_contingenza)
        print(f'Il p-value risultante dal test chi quadro sulla tabella di contingenza {column} - {target} è: {p}')
        print(f'Notazione non scientifica del p-value: {format(p, '.53f')}') #limite massimo decimali
        # calcolo indice di Cramer e stampa del valore
        cramer = contingency.association(tabella_contingenza, method='cramer')
        # pearson si sarebbe usato se le variabili fossero state quantitative

        print(f'L\'indice di Cramer calcolato sulla tabella di contingenza {column} - {target} è pari a: {cramer}')

        # di base da 0 a 0.1 è una correlazione debole, da 0.1 a 0.3 è una correlazione bassa, da 0.3 a 0.5 è una correlazione moderata
        # da 0.5 a 0.7 è una correlazione alta, da 0.7 a 0.9 è una correlazione molto alta, da 0.9 a 1 è una correlazione perfetta

        return tabella_contingenza

    # metodo per ottenere correlazione di Spearman (correlazione tra variabile quantitativa e categoriale)
    def correlazione_spearman(self, column, target):
        spearman_corr, p = spearmanr(self.dataframe[column], self.dataframe[target])
        print(f'La correlazione di Spearman risultante tra {column} e {target} risulta pari a: {spearman_corr}')
        print(f'Il p-value risultante dal test chi quadro sulla tabella di contingenza {column} - {target} è: {p}')

    # metodo per generare grafici a barre partendo da tabelle contingenza
    def grafici_contingenza(self):
        # generazione figura
        figura, cella = plt.subplots(1,2, figsize = (12,5))
        # 1o grafico - sopravvivenza per classe
        self.contingenza_classe.plot(kind='bar', ax=cella[0], color = ['red','green'])
        cella[0].set_title('Frequenza di Sopravvivenza per Classe Passeggero')
        cella[0].set_xlabel('Classe Passeggero')
        cella[0].set_ylabel('Frequenza')
        cella[0].legend(title='legenda')
        cella[0].tick_params(axis = 'x', rotation = 0) # disposizione etichette asse x in orizzontale
        # 2o grafico - sopravvivenza per genere
        self.contingenza_genere.plot(kind='bar', ax=cella[1], color=['red', 'green'])
        cella[1].set_title('Frequenza di Sopravvivenza per Genere Passeggero')
        cella[1].set_xlabel('Genere dei Sopravvissuti')
        cella[1].set_ylabel('Frequenza')
        cella[1].legend(title='legenda')
        cella[1].tick_params(axis='x', rotation=0)  # disposizione etichette asse x in orizzontale

        # show della figura
        plt.tight_layout() # aggiustamento spazi per evitare sovrapposizioni
        plt.show()

    # metodo per generare grafico a dispersione per dimostrare correlazione di SPearman
    def grafico_spearman(self):
        # generazione figura
        plt.figure(figsize=(8,5))
        # grafico unico (asse x = età, asse y = sopravvivenza)
        plt.scatter(self.dataframe['Età'], self.dataframe['Sopravvissuto'], alpha = 0.5, color = 'blue')
        plt.title('Distribuzione Età vs Sopravvivenza')
        plt.xlabel('Età del Passeggero')
        plt.ylabel('Sopravvissuto (0 = No - 1= Sì)')
        plt.show()

    # metodo per generare grafico a torta per ripartizione sopravvissuti-deceduti
    def grafico_ripartizione(self):
        # conteggio generale osservazioni
        sopravvissuti_deceduti = self.dataframe['Sopravvissuto'].value_counts()
        sopravvissuti_deceduti.plot(kind = 'pie', autopct = '%1.1f%%', startangle=90, colors=['red','green'],
                                    labels = sopravvissuti_deceduti.index.map({0:'Deceduti',1:'Sopravvissuti'}))
        plt.title('Distribuzione Sopravvissuti-Deceduti')
        plt.ylabel('')
        # show del grafico
        plt.show()

# utilizzo modello
modello = ModelloTitanic('../dataset_sistemati/data_04.csv')
# modello.analisi_generali(modello.dataframe)
# modello.analisi_valori_univoci(modello.dataframe_sistemato,
#                               ['Età','Fratelli/Coniugi', 'Genitori/Figli'])
# modello.individuazione_outliers(modello.dataframe_sistemato,'Genere')
# modello.dataframe_sistemato.to_csv('../dataset_sistemati/data_04.csv', index = False)