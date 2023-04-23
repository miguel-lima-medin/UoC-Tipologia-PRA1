# UoC-Tipología-PRA1
Tipología y ciclo de vida de los datos aula 1
Semestre Febrero 2023

Práctica 1: ¿Cómo podemos capturar los datos de la web?

Miguel Martínez Ruiz y Miguel Lima Medín

## Librerías a instalar
beautifulsoup4==4.12.2  
bs4==0.0.1  
certifi==2022.12.7  
charset-normalizer==3.1.0  
idna==3.4  
numpy==1.24.2  
pandas==2.0.0  
python-dateutil==2.8.2  
pytz==2023.3  
requests==2.28.2  
six==1.16.0  
soupsieve==2.4.1  
tzdata==2023.3  
urllib3==1.26. 

## Plugins requeridos
En PyCharm, activar PlantUML desde File->Settings->Languages & Frameworks->Markdown->Markdown Extensions->PlantUML

## Dataset en Zenodo
[https://doi.org/10.5281/zenodo.7856321](https://doi.org/10.5281/zenodo.7856321)

## Descripción de archivos

### Código
| Fichero                       | Contenido                                                                                                                                                                                                                                                                            |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| main.py                       | Fichero principal.<br/>Gestiona los argumentos recibidos y decide que función llamar para generar la lista de páginas a procesar<br/>Con la lista de páginas a procesar ejecuta un ciclo para extraer la información de cada página y generar el correspondiente fichero .csv y .log |
| read_available_commodities.py | Contiene las dos funciones que devuelven el listado de commodities a procesar:<br/>1) read_commodities_from_sitemap()<br/>2) read_commodities_from_menu()                                                                                                                            |
| extract_data_material.py      | Contiene la función que extrae la información de la página y devuelve un dataframe: scrape_data(url_to_process, verbose=False)                                                                                                                                                       |
| commodities_list.txt          | Permite definir la lista exacta de commodities que queremos extraer                                                                                                                                                                                                                  |

## Ejecutar el web scrapper
Se ejecuta llamando **main.py**

Se pueden consultar los parámetros con _main.py --help_

usage: main.py [-h] [--commodities_list COMMODITIES_LIST] [--download_from_sitemap] [--download_from_menu] [-v]
                                                                                                               
optional arguments:                                                                                            
  **-h, --help:**            show this help message and exit  
 
 **--commodities_list:** COMMODITIES_TEXT_FILE   
Name of the file containing the commodities list to process. Optional parameter. If not provided, then commodities_list.txt will be taken.  
  
**--download_from_sitemap:**  
If true, then commodities_list is ignored and the sitemap.xml will be explored for all commodities available as of now on the site.  
  
**--download_from_menu:**  If true, then commodities_list is ignored and the left menu of the webpage is explored with BeautifulSoup to identify the commodities.  
  
**-v, --verbose:**         Enable verbose output
