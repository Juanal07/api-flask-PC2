import requests
import re
from bs4 import BeautifulSoup

#a la hora de los INSERT en BBDD hay que evitar los duplicados buscando por el nombre del supermercado

def scraping():
    URL = 'https://www.supermercados-en-espana.com'
    #variables auxiliares
    '''linksProvincias = []
    linksMunicipios = []'''
    #supermercados = [] #datos a extraer: nombre del supermercado, direción, distancia y provincia

    searchProvincias(URL)
    '''searchMunicipios(URL)
    showSupermercados(URL, supermercados)'''

    #print(supermercados)

def searchProvincias(URL):
    provincia = input("Introduce el nombre de la provincia (con minúsculas y tilde): ")
    resultadoProvincia=False
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    tablaProvincias = soup.find_all('li') #almaceno todos los li's de la web
    for item in tablaProvincias:
        #obtengo el texto del link y el link para cada provicia
        name = item.find('a').text
        name = name.lower()
        name = re.sub('provincia de ','',name)
        name = re.sub('comunidad autónoma de ','',name)
        name = re.sub('ciudad autónoma de ','',name)
        name = re.sub('comunidad de ','',name)
        name = re.sub('comunidad foral de ','',name)
        name = re.sub('región de ','',name)
        name = re.sub('principado de ','',name)
        #name = re.sub(r'(.*) \/.*',,name)
        #print(name)

        if (name == provincia):
            link = item.find('a')['href']
            print(link)
            resultadoProvincia=True
            print("SUCCESS")
            searchMunicipios(URL,name,link)
            break

    if resultadoProvincia==False:
        print("Provincia no encontrada")       

    #return None

def searchMunicipios(URL,name,linkProvincia):
    linkProvincia = URL+linkProvincia
    resultadoMunicipio=False
    proviniciaPage = requests.get(linkProvincia)
    htmlProvinciaPage = BeautifulSoup(proviniciaPage.content, 'html.parser')
    aux = htmlProvinciaPage.find_all('table', width="700")
    tablaMunicipios = aux[0].find_all('a')

    municipio = input("Introduce el nombre del municipio (con minúsculas y tilde): ")
    for item in tablaMunicipios:
        #tupla = (item.text, item['href'], link[0])
        name = item.text
        name = name.lower()
        name = name[8:]
        #print(name)
        if (name == municipio):
            link = item['href']
            print(link)
            resultadoMunicipio=True
            print("SUCCESS")
            showSupermercados(URL,link)
            break
    if resultadoMunicipio==False:
        print("Municipio no encontrado") 


def showSupermercados(URL, link):
    supermercados = []
    linkMunicipio = URL + link
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
            tupla = (nombre, direccion, distancia)
            print(tupla)
            supermercados.append(tupla)

    except:
        print("\nERROR en ", linkMunicipio, "\n")
    
    #print(supermercados)
