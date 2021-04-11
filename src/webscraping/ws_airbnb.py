import requests
import re
from bs4 import BeautifulSoup

def scraping():
    URL = 'https://www.airbnb.es/s/madrid/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&checkin=2021-04-16&checkout=2021-04-23&source=structured_search_input_header&search_type=filter_change'
    mainURL = 'https://www.airbnb.es'
    nextPageBool = True
    opiniones = []
    while nextPageBool:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        casas = soup.find_all('div', class_="_8ssblpx")
        for casa in casas:
            name = casa.find('a', class_="_mm360j")
            name = name.attrs['aria-label']
            precio = casa.find('span', class_="_krjbj").text
            link = casa.find('a')["href"]
            media = float(soup.find('span', class_="_10fy1f8").text)
            tupla = (name,precio,link,media)
            opiniones.append(media)
            print(tupla)
        #obtengo la clase del boton activo, busco el siguiente hijo y compruebo si tiene link o es boton
        actualPage = soup.find(class_="_15k0tg7v")
        lastTag = actualPage.next_sibling.has_attr('href')
        if not lastTag:
            nextPageBool=False
        else:
            nextPage = actualPage.next_sibling["href"]
            URL = mainURL + nextPage
    #hago la media de todas las noticias
    total = 0
    for opinion in opiniones:
        total = total + opinion
    mediaFinal = total/len(opiniones)
    print("\nLa media final es ",mediaFinal)