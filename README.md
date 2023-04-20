# UoC-Tipologia-PRA1
Tipología y ciclo de vida de los datos aula 1
Semestre Febrero 2023

Práctica 1: ¿Cómo podemos capturar los datos de la web? de M2.851

Miguel Martínez Ruíz y Miguel Lima Medín

## Librerías a instalar
pip install lxml
pendiente de completar esta lista

## Ejecutar el web scrapper
Se ejecuta llamando **main.py**

Se pueden consultar los parámetros con _main.py --help_

usage: main.py [-h] [--commodities_list COMMODITIES_LIST] [--download_all_commodities DOWNLOAD_ALL_COMMODITIES] [-v]

options:
  -h, --help            show this help message and exit
  --commodities_list COMMODITIES_LIST
                        Name of the file containing the commodities list to process. Optional parameter. If not
                        provided, then commodities_list.txt will be taken.
  --download_all_commodities DOWNLOAD_ALL_COMMODITIES
                        If true, then commodities_list is ignored and the sitemap.xml will be explored for all
                        commodities available as of now on the site.
  -v, --verbose         enable verbose output
