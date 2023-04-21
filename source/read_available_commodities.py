import requests
from bs4 import BeautifulSoup
def read_commodities_from_sitemap():
    # Descargar sitemap.xml
    sitemap_url = "https://www.indexmundi.com/sitemap.xml"
    sitemap = requests.get(sitemap_url).text

    # Encontrar URLs con "commodities/?commodity="
    # TODO: Idealmente debería ser "xml", pero no me funcionó. Con html lo lee, pero es una ñapa
    soup = BeautifulSoup(sitemap, "html")

    urls = [loc.text for loc in soup.find_all("loc") if "commodities/?commodity=" in loc.text]

    # Extraer el nombre de cada commodity de cada URL
    commodities = []
    for url in urls:
        commodity = url.split("commodity=")[1].split("&")[0].capitalize()
        if commodity not in commodities:
            commodities.append(commodity)

    return commodities

def read_commodities_from_menu():

    url = "https://www.indexmundi.com/commodities/?"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, features="html.parser")

    # Creamos una lista de commodities vacía y guardamos los enlaces que contengan la etiqueta a
    # con un atributo href y la cadena "?commodity="
    commodity_links = []
    for link in soup.find_all('a'):
        if link.get('href') and "?commodity=" in link.get('href'):
            commodity_links.append(link)

    # Iteramos sobre los enlaces para extraer los nombres de las commodities
    commodities = []
    for link in commodity_links:
        commodity_name = link['href'].split("?commodity=")[1]
        commodities.append(commodity_name)

    return commodities