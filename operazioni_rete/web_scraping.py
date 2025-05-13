import pandas as pd
import pymysql
import requests
from bs4 import BeautifulSoup

try:
    risposta = requests.get('https://www.gdapplicazioni.it/views/tutorial-gratuiti.php')
    html = risposta.text
    # print(html)

    # istanziazione oggetto scraper(riesce ad eseguire un parsing)
    scraper = BeautifulSoup(html, 'html.parser')

    # ottenimento dei tag div contenenti i testi dei titoli
    div_titoli = scraper.find_all(name='div', class_='col-md-9 mt-3')
    # print(div_titoli)
    # ottenimento dei testi dei tag div dei titoli
    titoli = []
    for div in div_titoli:
        titolo = div.get_text()
        titoli.append(titolo.replace('\n',"").strip())
    # print(titoli)

    # ottenimento dei tag a contenenti gli url per i tutorial
    a_url = scraper.find_all(name='a', class_='btn btn-primary btn-sm mt-3')
    # print(a_url)

    # ottenimento dei valori href del tag a contenenti gli url del tutorial
    urls = []
    for a in a_url:
        url = a.get('href')
        urls.append(url)
    # print(urls)

    # generazione di un dataframe con i dati acquisiti mediante scraping
    dataframe = pd.DataFrame({'titoli': titoli, 'urls': urls})
    print(dataframe.to_string())

    # registrazione intero dataframe nel database
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        database= 'scraping'
    )
    with connection:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO tutorials (titoli, urls) VALUES (%s,%s)'
            for _, row in dataframe.iterrows():
                cursor.execute(sql, tuple(row))
            connection.commit()
except Exception as e:
    print(e)