import requests
import re
from bs4 import BeautifulSoup

def scraping():
    #URL = 'https://elpais.com/buscador/?qt=ios&sf=0&np=1&bu=ep&of=html'
    URL = 'https://www.airbnb.es/s/madrid/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&checkin=2021-04-16&checkout=2021-04-23&source=structured_search_input_header&search_type=filter_change'
    mainURL = 'https://www.airbnb.es'
    '''page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup)'''
    nextPageBool = True
    i=0
    while nextPageBool:
        #print(URL)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        #print(soup)
        # test = soup.has_attr
        nextPage = soup.find('a', class_="_1y623pm")["href"]
        #print(nextPage)
        URL = mainURL + nextPage
        '''noticias = soup.find_all('div', class_="noticia")
        for noticia in noticias:
            titulo = noticia.find('a', title_="Ver noticia").text
            link = noticia.find('a', title_="Ver noticia")["href"]
            print(titulo," ",link)'''
        casas = soup.find_all('div', class_="_8ssblpx")
        for casa in casas:
            name = casa.find('a', class_="_mm360j")
            name = name.attrs['aria-label']
            #print(name)
            precio = casa.find('span', class_="_krjbj").text
            #print(precio)
            link = casa.find('a')["href"]
            tupla = (name,precio,link)
            print(tupla)
            #break
        #en ultima pagina el elemento siguiente al activo es un boton, intentar tirar de ahi
        actualPage = soup.find(class_="_15k0tg7v")
        print(actualPage.next_sibling)
        lastTag = actualPage.next_sibling.has_attr('href')
        print(lastTag)
        #print(actualPage.next)
        if not lastTag:
            nextPageBool=False
        #i=i+1