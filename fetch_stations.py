from requests import get # 1
import json # 2
from pprint import pprint # 3

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/2599682' # Присвоїти змінній url посилання на дані конкретної метеостанції

weather = get(url).json()['items'] # взяти дані з посилання, обробити їх як json файл та записати у вигляді словника
pprint(weather) # вивести дані у зручному форматі