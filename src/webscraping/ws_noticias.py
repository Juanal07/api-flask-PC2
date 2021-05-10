from bs4 import BeautifulSoup
import requests
import re

#librerías de IA
import pandas as pd
import string
from nltk import word_tokenize, download
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
download('punkt')

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import joblib #para exportar el modelo
import pickle

def scraping():
    Pueblo = input('Introduzca un municipio: ')
    #Pueblo = 'villaviciosa de odon'
    url = 'https://www.20minutos.es/busqueda//?q='+Pueblo+'&sort_field=&category=&publishedAt%5Bfrom%5D=&publishedAt%5Buntil%5D='
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find("section", attrs={"class": "content content-100"})
    links1 = links.find_all('div', class_='media-content')
    i=1
    noticias = []
    for  item in links1:
        link2 = item.find('a')['href']
        # print(link2)
        # print('----------------------'+str(i)+'------------------------------')
        # ws_articulo(link2)
        # ws_fecha(link2)
        noticia = ws_texto(link2)
        noticias.append(noticia)
        i+=1
    # print(noticias)

    # Ahora empezamos a aplicar el IA
    noticias2 = [] # Quitamos las noticias que por fallo generen una posición vacía
    for i in noticias:
        if i!="":
            noticias2.append(i)
    # print(noticias2)
    # Proceso de limpieza del array de textos
    spanish_stemmer = SnowballStemmer('spanish')
    corpus = []
    for texto in noticias2:
        clean_text = re.sub("[%s]" % re.escape(string.punctuation), " ", texto)
        clean_text= clean_text.lower()
        clean_text = re.sub('\w*\d\w*', ' ', clean_text)
        tokenized = word_tokenize(clean_text)
        for j in range(len(tokenized)):
            tokenized[j]=format(spanish_stemmer.stem(tokenized[j]))
        stemmed = ' '.join(tokenized)
        corpus.append(stemmed)
    # print(corpus)

    # Cargamos el texto de stop words en castellano, lo mostramos
    # with open('src\webscraping\stopword.txt', 'r') as file:
    #     my_stopwords=[file.read().replace('\n', ',')]
    # print(my_stopwords)
    stop_es = stopwords.words('spanish')

    # Creamos Matrix TF-IDF aplicando nuestras stop words y la mostramos
    # cv_tfidf = TfidfVectorizer(analyzer='word', stop_words = stop_es)
    tf1 = pickle.load(open("src\webscraping\/tfidf1.pkl", 'rb'))
    # Create new tfidfVectorizer with old vocabulary
    tf1_new = TfidfVectorizer(analyzer='word', stop_words = stop_es, vocabulary = tf1.vocabulary_)
    X_tf1 = tf1_new.fit_transform(corpus)
    # X_tfidf = tf1.fit_transform(corpus).toarray()
    # pd.DataFrame(X_tfidf, columns=cv_tfidf.get_feature_names())
    # text_features = tf1.transform(corpus)
    model = pickle.load(open('src\webscraping\modelo.pickle', 'rb'))
    vectorizedCorpus = model.transform(corpus)
    predictions = model.predict(vectorizedCorpus)
    print("  - Predicted as: '{}'".format(predictions))

def ws_articulo(link):
    try:
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        #print(soup)
        titulo = soup.find('h1', class_='article-title')
        titulo = titulo.text
        print('Titulo: '+ titulo)   

    except:
        print('No se pudo scrapear')
    return None 

def ws_fecha(noticia):
    try:
        page = requests.get(noticia)
        soup = BeautifulSoup(page.content, 'html.parser')
        #print(soup)
        fecha = soup.find('span', class_='article-date')
        fecha = fecha.text
        print('Fecha: ' + fecha)   

    except:
        print('No se pudo scrapear')
    return None 

def ws_texto(titulo):
    try:
        page = requests.get(titulo)
        soup = BeautifulSoup(page.content, 'html.parser')
        texto = soup.find('div', class_="article-text")
        texto = soup.find_all('p', class_='paragraph')
        total = ""
        for  textos in texto:
            #texto1 = textos.find('a')['href']
            total += textos.text
            # print (textos.text)
    except:
        print('No se pudo scrapear')
    return total


'''
if __name__ == '__main__':
    scraping()          

'''