import requests
from bs4 import BeautifulSoup

#a la hora de los INSERT en BBDD hay que evitar los duplicados buscando por el nombre del supermercado

def scraping():
    URL = 'https://www.supermercados-en-espana.com/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)


    #datos a extraer: nombre del supermercado, direción, municipio, código postal y provincia

    linksProvincias=[]
    URLsProvincias=[]
    linksMunicipios=[]
    tablaProvincias = soup.find_all('li') #almaceno todos los li's de la web
    #linksProvincias = tablaProvincias.find_all('a')['href']
    for item in tablaProvincias:
        '''print(item)
        print("Provincia: ", item.find('a').text)
        print("Link: ", item.find('a')['href'])'''
        #obtengo el texto del link y el link para cada provicia
        tupla = (item.find('a').text, item.find('a')['href'])
        linksProvincias.append(tupla)
        URLsProvincias.append(URL+item.find('a')['href'])
    
    #print(URLsProvincias)
    #print(len(linksProvincias)) 
    #forma de acceder a la posición 5 del array, pos 1 de la tupla     
    #print(linksProvincias[5][1])

    for link in URLsProvincias:
        proviniciaPage = requests.get(link)
        htmlProvinciaPage = BeautifulSoup(proviniciaPage.content, 'html.parser')
        aux = htmlProvinciaPage.find_all('table', width="700")
        #aux = htmlProvinciaPage.find_all('table', valign="top")
        #print(aux.find_all('a'))
        tablaMunicipios = aux[0].find_all('a')
        #print(tablaMunicipios)
        for item in tablaMunicipios:
            tupla = (item.text, item['href'])
            #print(tupla)
            linksMunicipios.append(tupla)
            #print(item.find_all('a'))'''
        #aux2 = aux.find_all(align='top')
        #municipios1 = aux[len(aux)-3]
        #municipios2 = aux[len(aux)-2]

        print(linksMunicipios)
        '''for item in municipios1:
            print(item)
            #print("Provincia: ", item.find('a').text)
            print("Link: ", item.find('a')['href'])'''





        #para mostrar solo los resultados de una página
        break


    return None