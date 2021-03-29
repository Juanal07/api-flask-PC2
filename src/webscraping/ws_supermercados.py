import requests
from bs4 import BeautifulSoup

def scraping():
    URL = 'https://www.supermercados-en-espana.com/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup)

    

    return None