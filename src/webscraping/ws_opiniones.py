import requests
import re
from bs4 import BeautifulSoup

def scraping():

    pueblo = 'villaviciosa de odón'
    provincia = 'madrid'
    URL = 'http://www.buscorestaurantes.com/filtrar-ubicacion-en/'+provincia
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup = soup.find(attrs={"class": "block-level"})
    # print(soup)
    soup = soup.find_all('li')

    for item in soup:
        link = item.find('a')['href']
        name = item.find('a').text
        # print(name)
        name = name.lower()
        name = re.sub('\t', '', name) 
        name = re.sub('\n', '', name)
        name = re.sub('restaurantes en ', '', name)
        if (name == pueblo):
            ws_pueblo(link)
        # dupla = (name, link)
        # duplas.append(dupla)
        # print(dupla)
    return None 

def ws_restaurant(link):

    URL = link
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup = soup.find_all(attrs={"class": "excerpt"})
    for item in soup:
        opinion = item.text
        print(opinion)
    return None

def ws_pueblo(link):

    URL = link
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup = soup.find(attrs={"class": "listado-items"})
    soup = soup.find_all(attrs={"class": "listing-item-title"})
    for item in soup:
        link = item.a['href']
        ws_restaurant(link)
        # print(link)
    # print(soup)
    return None





