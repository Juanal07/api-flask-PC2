import requests
from bs4 import BeautifulSoup

def scraping():
    headers = {'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1', 'accept-encoding': 'gzip, deflate, br'}
    URL = 'https://www.eltenedor.es/search/?cityId=328022'
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    siguiente = soup.find(class_="_3bkrI").findChildren('li')
    numparada = int(siguiente[-1].text)
    mediapag = 0
    for i in range(1, numparada+1):
        page = requests.get(URL + '&p=' + str(i))
        soup2 = BeautifulSoup(page.content, 'html.parser')
        restaurantes = soup2.find_all(class_="card eucs7wk1 css-mreu2p e6vs4hd0")
        nota = 0
        cont = 1
        print(soup2)
        for j in restaurantes:
            link = j.find('a', class_="eucs7wk6 css-182wgzx ejesmtr0")['href']
            opiniones = tenedor(link)
            nota += mediaOpiniones(opiniones)
            cont += 1
        mediapag += nota/cont
    media = mediapag/numparada
    print('La media de los restaurantes de Madrid es: ' + str(media))
    return None

def tenedor(link):
    link = 'https://www.eltenedor.es' + link
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    opiniones = soup.find('a', class_="css-1dlyfwd e6afjz61")['href']
    return opiniones

def mediaOpiniones(link):
    link = 'https://www.eltenedor.es' + link
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    nombre = soup.find('h1', class_="gl3M_ css-k6vko4 e1l48fgb0")
    print(nombre.text)
    siguiente = soup.find(class_="_3bkrI").findChildren('li')
    numparada = int(siguiente[-1].text)
    mediapag = 0
    for i in range(1, numparada+1):
        page = requests.get(link + '?p=' + str(i))
        soup = BeautifulSoup(page.content, 'html.parser')
        soup = soup.find_all(class_='_2qEfW css-2tzvei e1l48fgb0')
        nota = 0
        cont = 0
        for j in soup:
            nota += int(j.text)
            cont += 1
        mediapag += nota/cont 
    media = mediapag/numparada
    print(str(media))
    print('----------------------------------------------')
    return media


