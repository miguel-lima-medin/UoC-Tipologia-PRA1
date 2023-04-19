import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data(url_to_process):

    page = requests.get(url_to_process)

    soup = BeautifulSoup(page.content, features="html.parser")

    # print(soup.prettify())

    title = soup.title.string
    print(title)

    table = soup.find(class_ = 'tblData')
    rows = table.find_all('tr')

    # Crea una lista vacía para contener los datos de la tabla
    datos = []

    # Itera a través de las filas y extrae los datos de cada columna
    for row in rows:
        # Encuentra todas las etiquetas 'td' en la fila
        columnas = row.find_all('td')

        # Si la fila tiene columnas
        if len(columnas) > 0:
            # Extrae los datos de cada columna
            month = columnas[0].get_text()
            price = columnas[1].get_text()
            change = columnas[2].get_text()

            # Crea un diccionario para contener los datos de la fila
            fila_dict = {'Month': month, 'Price': price, 'Change': change}

            # Agrega el diccionario a la lista de datos
            datos.append(fila_dict)

    # Crea el DataFrame de pandas a partir de la lista de datos
    df = pd.DataFrame(datos)

    # # Convierte los tipos de datos adecuados para las columnas Price y Change
    # df['Price'] = pd.to_numeric(df['Price'])
    # df['Change'] = df['Change'].str.rstrip('%').astype('float') / 100

    return df