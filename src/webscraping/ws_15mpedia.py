import requests
from bs4 import BeautifulSoup

def shield(link):
    URL = 'https://15mpedia.org' + link
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    link = soup.find('a', class_="image")['href']
    page = requests.get('https://15mpedia.org' + link)
    soup = BeautifulSoup(page.content, 'html.parser')
    link = soup.find(class_="fullImageLink")
    link = link.find('a')['href']
    print('Escudo - ' + link)
    return None

def scraping():
    URL = 'https://15mpedia.org/w/index.php?title=Especial:Ask&offset=0&limit=8134&q=%5B%5BPage+has+default+form%3A%3AMunicipio%5D%5D+%5B%5Bpa%C3%ADs%3A%3AEspa%C3%B1a%5D%5D&p=format%3Dtable%2Fmainlabel%3DMunicipio&po=%3F%3DMunicipio%23%0A%3FComarca%23-%0A%3FProvincia%0A%3FComunidad+aut%C3%B3noma%3DCC.AA.%0A%3FAltitud%3DAltitud+%28m.s.n.m.%29%0A%3FSuperficie%3DSuperficie+%28km%C2%B2%29%0A%3FPoblaci%C3%B3n+en+2019%3DPoblaci%C3%B3n+%282019%29%0A%3FDensidad+de+poblaci%C3%B3n%3DDensidad+%28hab.%2Fkm%C2%B2%29%0A&sort=nombre&order=asc'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    Municipios = []
    tabla = soup.find("tbody")
    tabla = tabla.find_all("tr")
    for i in tabla:
        #----Municipio----
        municipio = i.find(class_="Municipio")
        print('Municipio - ' + municipio.text)
        #----Escudo----
        link = municipio.find('a')['href']
        escudo = shield(link)
        #----Comarca----
        comarca = i.find(class_="Comarca")
        if comarca == None:
            comarca = 'Comarca - ' 
            print(comarca)
        else:
            print('Comarca - ' + comarca.text)
        #----Provincia----
        provincia = i.find(class_="Provincia")
        print('Provincia - ' + provincia.text)
        #----CCAA----
        CCAA = i.find(class_="CC.AA.")
        print('CCAA - ' + CCAA.text)
        #----Altitud----
        altitud = i.find(class_="Altitud-(m.s.n.m.)")
        if altitud == None:
            altitud = 'Altitud - ' 
            print(altitud)
        else:
            print('Altitud - ' + altitud.text + ' m.s.n.m')
        #----Superficie----
        superficie = i.find(class_="Superficie-(km²)")
        if superficie == None:
            superficie = 'Superficie - ' 
            print(superficie)
        else:
            print('Superficie - ' + superficie.text + ' km²')
        #----Poblacion----
        poblacion = i.find(class_="Población-(2019)")
        if poblacion == None:
            poblacion = 'Poblacion - ' 
            print(poblacion)
        else:
            print('Poblacion - ' + poblacion.text + ' habitantes ')
        #----Densidad----
        densidad = i.find(class_="Densidad-(hab./km²)")
        if densidad == None:
            densidad = 'Densidad - ' 
            print(densidad)
        else:
            print('Densidad - ' + densidad.text + ' hab./km²')
        print('-----------------------------------')
    return None
