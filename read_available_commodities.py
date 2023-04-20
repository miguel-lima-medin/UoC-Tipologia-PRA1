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