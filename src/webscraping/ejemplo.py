# 15mpedia o wikipedia
# https://www.eltenedor.es/  # RESTAURANTES
# https://www.supermercados-en-espana.com/ # SUPERMERCADOS
# https://www.mscbs.gob.es/ciudadanos/centros.do # CENTROS DE SALUD
# https://flo.uri.sh/visualisation/667558/embed # COLEGIOS
# https://datos.gob.es/es/catalogo/ea0003337-estaciones-listado-completo1 #

import re
import requests
from bs4 import BeautifulSoup

def scrap():
    i = 1
    contador = 0
    while i < 27:
        URL = 'https://votainteligente.cl/propuestas/?page='+str(i)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(id='posts')
        job_elems = results.find_all('div', class_='post')
        for job_elem in job_elems:
            try:
                category = job_elem.find('a')['href']
                category = re.search("clasification=(.*)", category)
                category = category.group(1)
                title = job_elem.find('h4')
                title = title.text
                title = re.sub("/", "-", title)
                leer_mas = job_elem.find('a', class_='btn btn-blue pull-right')['href']
                URL = 'https://votainteligente.cl'+leer_mas
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, 'html.parser')
                cuerpo = soup.find('div', class_='col-md-12')
                cuerpo = cuerpo.find('p')
                cuerpo = cuerpo.text
            except:
                print ("Error: ")
