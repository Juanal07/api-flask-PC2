import requests
from bs4 import BeautifulSoup

#a la hora de los INSERT en BBDD hay que evitar los duplicados buscando por el nombre del supermercado

def scraping():
    URL = 'https://www.supermercados-en-espana.com'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    #variables auxiliares
    linksProvincias = []
    linksMunicipios = []
    supermercados = [] #datos a extraer: nombre del supermercado, direción, distancia y provincia

    tablaProvincias = soup.find_all('li') #almaceno todos los li's de la web
    for item in tablaProvincias:
        #obtengo el texto del link y el link para cada provicia
        tupla = (item.find('a').text, item.find('a')['href'])
        linksProvincias.append(tupla)
        #break

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
        #break

    #print(linksProvincias)
    #print(linksMunicipios)

    #obtengo los supermercados de cada municipio
    for municipio in linksMunicipios:
        linkMunicipio = URL + municipio[1]
        #print(municipio[0]," ",linkMunicipio)
        try:
            municipioPage = requests.get(linkMunicipio)
            htmlMunicipio = BeautifulSoup(municipioPage.content, 'html.parser')
            divsSupers = htmlMunicipio.find_all('div', style="text-align:left;background:#E9F2F2;border:1px solid #bad8db;margin-left:5px;margin-bottom:5px;padding:5px;min-height:50px;width:300px;")
            #print(divsSupers)
            for supermercado in divsSupers:
            #obtengo los datos para cada uno de los supermercados
                nombre = supermercado.find('b').text
                divMunicipio = supermercado.contents
                distancia = divMunicipio[3][13:len(divMunicipio[3])-3]
                direccion = divMunicipio[8]

                #muchos problemas codigos postales con direcciones inconsistentes y posiciones en sitios diferentes del div
                #intentos para obtener el municipio y codigo postal, finalmente se descarta
                '''codPostal = divMunicipio[10][:5]
                codPostal = municipio[0][:5] #para provenientes de link
                codPostal += "divMunicipio"
                #municipio = divMunicipio[10][6:]
                municipio = municipio[0][8:] #para provenientes de link
                municipio = "divMunicipio"+municipio'''

                '''try:
                    codPostal = divMunicipio[10][:5]
                    municipio = divMunicipio[10][6:]
                except:
                    print("ERROR")
                    codPostal = municipio[0][:5]
                    municipio = municipio[0][8:]'''
                '''print(codPostal)
                print(municipio)'''

                #meto datos en la lista: nombre del supermercado, direción, distancia y provincia
                tupla = (nombre, direccion, distancia, municipio[2])
                print(tupla)
                supermercados.append(tupla)

        except:
            print("\nERROR en ", linkMunicipio, "\n")


    #print(supermercados)

    #forma de acceder a la posición 5 del array, pos 1 de la tupla     
    #print(linksProvincias[5][1])

    return None