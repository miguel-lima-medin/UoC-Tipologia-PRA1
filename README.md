# UoC-Tipologia-PRA1
Tipología y ciclo de vida de los datos aula 1
Semestre Febrero 2023

Práctica 1: ¿Cómo podemos capturar los datos de la web? de M2.851

Miguel Martínez Ruíz y Miguel Lima Medín

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
