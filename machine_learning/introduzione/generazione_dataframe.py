import pandas as pd

# dichiarazione di 2 liste + dizionario di inclusione
nomi = ['Mario', 'Gianni', 'Laura', 'Sara']
eta = [50, 32, 24, 18]
utenti = {'Nome': nomi, 'Età': eta}

# generazione dataframe mediante dizionario
df_uno = pd.DataFrame(utenti)
print('Dataframe Uno', df_uno, sep='\n')

# generazione dataframe mediante lista (con iterazione)
df_due = pd.DataFrame([[nomi[i], eta[i]] for i in range(len(nomi))], columns = ['Nome','Età'])
print('Dataframe Due', df_due,sep = '\n')

# generazione dataframe mediante lista (con trasposizione)
df_tre = pd.DataFrame([nomi, eta]).T
df_tre.columns = ['Nome', 'Età']
print('Dataframe Tre', df_tre, sep='\n')

# generazione dataframe mediante file csv (con intestazione originale)
df_quattro = pd.read_csv('../dataset/data_01.csv')
print('Dataframe Quattro: ', df_quattro, sep = '\n')

# generazione dataframe mediante file csv (con intestazione modificata)
df_cinque = pd.read_csv('../dataset/data_01.csv', skiprows=1, names=['i','n','c','u','p']) # skiprows salta la prima riga, names riassegna i nomi delle colonne
print('Dataframe Cinque: ', df_cinque, sep = '\n')

# generazione dataframe mediante file json (con intestazione originale)
df_sei = pd.read_json('../dataset/data_02.json')
print('Dataframe Sei: ', df_sei, sep = '\n')

# generazione dataframe mediante file json (con intestazione modificata)
df_sette = pd.read_json('../dataset/data_02.json')
df_sette.columns = ['i','n','c','u','p']
df_sette.rename(columns={'p':'pwd'}, inplace = True)
print('Dataframe Sette: ', df_sette, sep = '\n')