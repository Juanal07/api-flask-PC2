import requests
from bs4 import BeautifulSoup

def scraping():
    URL = 'https://www.supermercados-en-espana.com/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)

    i=0
    linksProvincias=[]
    tablaProvincias = soup.find_all('li')
    #linksProvincias = tablaProvincias.find_all('a')['href']
    for item in tablaProvincias:
        '''print(item)
        print("Provincia: ", item.find('a').text)
        print("Link: ", item.find('a')['href'])'''
        tupla = (item.find('a').text, item.find('a')['href'])
        linksProvincias.append(tupla)
        
     #forma de acceder a la posición 5 del array, pos 1 de la tupla     
    print(linksProvincias[5][1])

    return None