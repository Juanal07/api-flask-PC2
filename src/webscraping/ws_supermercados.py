import requests
from bs4 import BeautifulSoup

#a la hora de los INSERT en BBDD hay que evitar los duplicados buscando por el nombre del supermercado

def scraping():
    URL = 'https://www.supermercados-en-espana.com'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    #datos a extraer: nombre del supermercado, direción, municipio, código postal y provincia
    dataset = []
    #variables auxiliares
    linksProvincias = []
    linksMunicipios = []
    supermercados = []

    tablaProvincias = soup.find_all('li') #almaceno todos los li's de la web
    #linksProvincias = tablaProvincias.find_all('a')['href']
    for item in tablaProvincias:
        #obtengo el texto del link y el link para cada provicia
        tupla = (item.find('a').text, item.find('a')['href'])
        linksProvincias.append(tupla)

    for link in linksProvincias:
        linkProvincia = URL+link[1]
        proviniciaPage = requests.get(linkProvincia)
        htmlProvinciaPage = BeautifulSoup(proviniciaPage.content, 'html.parser')
        aux = htmlProvinciaPage.find_all('table', width="700")
        tablaMunicipios = aux[0].find_all('a')
        for item in tablaMunicipios:
            tupla = (item.text, item['href'], link[0])
            linksMunicipios.append(tupla)
        #para mostrar solo los resultados de una provincia
        break

    #print(linksProvincias)
    #print(linksMunicipios)

    #obtengo los supermercados de cada municipio
    for municipio in linksMunicipios:
        #print(municipio[0])
        linkMunicipio = URL + municipio[1]
        #print(linkMunicipio)
        municipioPage = requests.get(linkMunicipio)
        htmlMunicipio = BeautifulSoup(municipioPage.content, 'html.parser')
        #print(htmlMunicipio.find('title'))
        #print(htmlMunicipio)
        divsSupers = htmlMunicipio.find_all('div', style="text-align:left;background:#E9F2F2;border:1px solid #bad8db;margin-left:5px;margin-bottom:5px;padding:5px;min-height:50px;width:300px;")
        #print(divsSupers)
        for supermercado in divsSupers:
            nombre = supermercado.find('b').text
            #print(supermercado)
            test = supermercado.contents
            #print(test)
            #print("\nDirección: ",test[8],"\nMunicipio: ", test[10])
            #muchos problemas codigos postales con direcciones inconsistentes y posiciones en sitios diferentes del div
            #print(test[10])

            '''#direccion = test[8]
            #codPostal = test[10][:5]
            codPostal = municipio[0][:5] #para provenientes de link
            codPostal += "test"
            #municipio = test[10][6:]
            municipio = municipio[0][8:] #para provenientes de link
            municipio = "test"+municipio
            print(codPostal)
            print(municipio)'''

            '''try:
                codPostal = test[10][:5]
                municipio = test[10][6:]
                print(codPostal)
                print(municipio)
            except:
                print("ERROR")
                codPostal = municipio[0][:5]
                municipio = municipio[0][8:]
                print(codPostal)
                print(municipio)
            print(codPostal)
            print(municipio)'''

            #meto datos en la lista: nombre del supermercado, direción, municipio, código postal y provincia
            '''tupla = (nombre, direccion, municipio, codPostal, municipio[2])
            print(tupla)
            supermercados.append(tupla)'''


    #print(supermercados)

    #forma de acceder a la posición 5 del array, pos 1 de la tupla     
    #print(linksProvincias[5][1])


    return None