import requests
from bs4 import BeautifulSoup

def scraping():

    URL = 'https://15mpedia.org/w/index.php?title=Especial:Ask&offset=0&limit=1000&q=%5B%5BPage+has+default+form%3A%3AMunicipio%5D%5D+%5B%5Bpa%C3%ADs%3A%3AEspa%C3%B1a%5D%5D&p=format%3Dtable%2Fmainlabel%3DMunicipio&po=%3F%3DMunicipio%23%0A%3FComarca%23-%0A%3FProvincia%0A%3FComunidad+aut%C3%B3noma%3DCC.AA.%0A%3FAltitud%3DAltitud+%28m.s.n.m.%29%0A%3FSuperficie%3DSuperficie+%28km%C2%B2%29%0A%3FPoblaci%C3%B3n+en+2019%3DPoblaci%C3%B3n+%282019%29%0A%3FDensidad+de+poblaci%C3%B3n%3DDensidad+%28hab.%2Fkm%C2%B2%29%0A&sort=nombre&order=asc'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup)
    return None 

# 15mpedia o wikipedia
# https://www.eltenedor.es/  # RESTAURANTES
# https://www.supermercados-en-espana.com/ # SUPERMERCADOS
# https://www.mscbs.gob.es/ciudadanos/centros.do # CENTROS DE SALUD
# https://flo.uri.sh/visualisation/667558/embed # COLEGIOS
# https://datos.gob.es/es/catalogo/ea0003337-estaciones-listado-completo1 #

# i = 1
# contador = 0
# while i < 27:
#     URL = 'https://votainteligente.cl/propuestas/?page='+str(i)
#     page = requests.get(URL)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     results = soup.find(id='posts')
#     job_elems = results.find_all('div', class_='post')
#     for job_elem in job_elems:
#         try:
#             category = job_elem.find('a')['href']
#             category = re.search("clasification=(.*)", category)
#             category = category.group(1)
#             title = job_elem.find('h4')
#             title = title.text
#             title = re.sub("/", "-", title)
#             leer_mas = job_elem.find('a', class_='btn btn-blue pull-right')['href']
#             URL = 'https://votainteligente.cl'+leer_mas
#             page = requests.get(URL)
#             soup = BeautifulSoup(page.content, 'html.parser')
#             cuerpo = soup.find('div', class_='col-md-12')
#             cuerpo = cuerpo.find('p')
#             cuerpo = cuerpo.text
