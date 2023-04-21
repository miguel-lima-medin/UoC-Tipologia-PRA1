from datetime import datetime
import time
from dateutil.utils import today
import logging
import traceback
import random
import argparse
import os
# TODO: meter instalaciones en README.me

from extract_data_material import scrape_data
from read_available_commodities import read_commodities_from_sitemap

# Definimos los parámetros que se pueden usar para llamar a main.py
parser = argparse.ArgumentParser()
parser.add_argument('--commodities_list', type=str, help='Name of the file containing the commodities list to process. Optional parameter. If not provided, then commodities_list.txt will be taken.')
parser.add_argument('--download_from_sitemap', type=bool, help='If true, then commodities_list is ignored and the sitemap.xml will be explored for all commodities available as of now on the site.')
parser.add_argument('--download_from_menu', type=bool, help='If true, then commodities_list is ignored and the left menu of the webpage is explored with BeautifulSoup to identify the commodities.')
parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
args = parser.parse_args()

#Dependiendo de los parámetros usados, generamos una lista de commodities a procesar
if args.download_from_sitemap:
    commodities_to_process = read_commodities_from_sitemap()
else:
    if args.commodities_list is None:
        commodities_list_file = "commodities_list.txt"
    else:
        commodities_list_file = args.commodities_list

    if not os.path.exists(commodities_list_file):
        print(f"The specified file '{commodities_list_file}' does not exist.")
        exit(1)

    #Leemos las commodities del fichero
    with open(commodities_list_file, 'r') as f:
        commodities_to_process = [line.strip() for line in f]

if args.verbose:
    print("Se van a procesar las siguientes commodities:\n")
    logging.debug("Se van a procesar las siguientes commodities:\n")
    for commodity in commodities_to_process:
        print(commodity)
        logging.debug(commodity)

# Almacenamos constantes que usaremos más tarde para log y para nombres de ficheros
date_today_str = today().strftime("%Y_%m_%d")
logging.basicConfig(filename='main_' + date_today_str + '.log', level=logging.DEBUG)
base_url = "https://www.indexmundi.com/commodities/?commodity="

for commodity in commodities_to_process:
    # Pausa por un tiempo aleatorio entre 1 y 3 segundos para no sobrecargar el servidor
    sleep_time = random.uniform(1, 3)
    time.sleep(sleep_time)

    try:
        df = scrape_data(base_url + commodity, verbose=args.verbose)

        # TODO: probar a generar un Excel con varios tabs.
        # [see issue #4](https://github.com/miguel-lima-medin/UoC-Tipologia-PRA1/issues/4)
        # df.to_excel('Commodities_' + date_today_str + '.xlsx', sheet_name=commodity)

        # TODO: sea Excel o .csv tiene que guardarse en una carpeta separada. Hay que ver en el enunciado de la práctica la nomenclatura esperada
        df.to_csv(commodity + '_' + date_today_str + '.csv')
    except Exception as e:
        timestamp = datetime.now().strftime("%H:%M:%S")
        traceback.print_exc()
        logging.error(f"{timestamp} Error scraping data for {commodity}: {e}")