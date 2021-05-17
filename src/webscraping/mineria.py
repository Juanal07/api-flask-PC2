# Imports
import os
import pandas as pd
import re
import string
import matplotlib.pyplot as plt
import seaborn as sns

from nltk import word_tokenize, download
from nltk.stem import SnowballStemmer
download('punkt')

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import joblib #para exportar el modelo

# Creamos el array de textos y el array de categorias
x=[]
y=[]

# Cargamos el dataset
for cat in os.listdir('../newspaper-articles-main/'):
    for txt in os.listdir('../newspaper-articles-main/'+cat+'/'):
        with open ('../newspaper-articles-main/'+cat+'/'+txt, encoding = 'utf8') as f:
            x.append(f.read())
            y.append(cat)

# Mostramos el array de textos
print(x)
print(y)

# Pasamos el array de categorias a valores numericos
y_num=[]
value_des = 0
value_nodes = 0
for i in y:
    if i == 'Despoblacion':
        value_des+=1
        y_num.append(0)
    else:
        y_num.append(1)
        value_nodes+=1

# Mostramos el array de categorias por numero
print(y_num)

# Mostramos numero de textos por categoria
names = ['Despoblacion', 'No despoblacion']
values = [value_des, value_nodes]
plt.bar(names, values)

# Proceso de limpieza del array de textos
spanish_stemmer = SnowballStemmer('spanish')
corpus = []
for texto in x:
    clean_text = re.sub("[%s]" % re.escape(string.punctuation), " ", texto)
    clean_text= clean_text.lower()
    clean_text = re.sub('\w*\d\w*', ' ', clean_text)
    tokenized = word_tokenize(clean_text)
    for j in range(len(tokenized)):
        tokenized[j]=format(spanish_stemmer.stem(tokenized[j]))
    stemmed = ' '.join(tokenized)
    corpus.append(stemmed)

# Cargamos el texto de stop words en castellano, lo mostramos
with open('../stopword.txt', 'r') as file:
    my_stopwords=[file.read().replace('\n', ',')]
print(my_stopwords)

# Creamos Matrix TF-IDF aplicando nuestras stop words y la mostramos
cv_tfidf = TfidfVectorizer(analyzer='word', stop_words = my_stopwords)
X_tfidf = cv_tfidf.fit_transform(corpus).toarray()
pd.DataFrame(X_tfidf, columns=cv_tfidf.get_feature_names())

# Dividimos nuestros datos en train/test al 80/20 y mostramos que categorias hay en cada grupo
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y_num, test_size=0.2, random_state=0)
print(y_train)
print(y_test)

# Para los modelos que queremos probar: entrenamos, testeamos, mostramos la accuracy,
# la classification reoprt y la confusion matrix
model = DecisionTreeClassifier(random_state=6)
grid_param = {
    'criterion': ['gini', 'entropy'],
    'splitter': ['best', 'random']
}
gd_sr = GridSearchCV(estimator=model,
                     param_grid=grid_param,
                     scoring='accuracy',
                     cv=3,
                     n_jobs=-1)
gd_sr.fit(X_train, y_train)
joblib.dump(gd_sr, 'modelo.pkl') #Guardo el modelo
best_parameters = gd_sr.best_params_
print(best_parameters)
best_result = gd_sr.best_score_
print('Accuracy train/validation: ', best_result)
prediction=gd_sr.predict(X_test)
acc = accuracy_score(y_test, prediction)
print("Accuracy test: " + str(acc) + '\n')
print(classification_report(y_test, prediction))
print(confusion_matrix(y_test, prediction))

# Mostramos la confusion matrix con mapa de calor
conf_mat = confusion_matrix(y_test, prediction)
sns.heatmap(conf_mat, annot=True, fmt='d',
            xticklabels=['despoblacion','no despoblacion'], yticklabels=['despoblacion','no despoblacion'])
plt.ylabel('Actual')
plt.xlabel('Predicted')

# Clasificamos textos al momento
texts = ["Los pueblos de la españa vaciada",
         "El capitan tsubasa marca un gol para el equipo de japon",
         "trump deja la casa blanca",
         "beyonce saca un nuevo disco y es exito en asia",
         "el pueblo de mi abuela no tiene gente"]

# Proceso de limpieza del array de textos
spanish_stemmer = SnowballStemmer('spanish')
corpus = []
for texto in texts:
    clean_text = re.sub("[%s]" % re.escape(string.punctuation), " ", texto)
    clean_text= clean_text.lower()
    clean_text = re.sub('\w*\d\w*', ' ', clean_text)
    tokenized = word_tokenize(clean_text)
    for j in range(len(tokenized)):
        tokenized[j]=format(spanish_stemmer.stem(tokenized[j]))
    stemmed = ' '.join(tokenized)
    corpus.append(stemmed)

text_features = cv_tfidf.transform(corpus)
predictions = gd_sr.predict(text_features)
for text, predicted in zip(texts, predictions):
  print('"{}"'.format(text))
  print("  - Predicted as: '{}'".format(predicted))
  print("")
