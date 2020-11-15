# There is GUI for fetch local weather program
from PySimpleGUI import PySimpleGUI as sg

from FindClosest import find_closest 

import json # import json processer
from requests import get # import get library
from pprint import pprint # import updated print()

# stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'

my_lat = 50.29007
my_lon = 25.37424

def get_weather(my_lat, my_lon):  
    weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'
    closest_stn = find_closest(my_lat, my_lon) # call function and save result to variable
    weather = weather + str(closest_stn) # convert int to string
    my_weather = get(weather).json()['items'] # send GET request
    return my_weather # return metrics

def bs(message): # beautiful separate
    print("------------------------------------------")
    print(" "+message)
    print("------------------------------------------")

def isReal(check):
    try:
        # validate it's a float
        float(check)
        return True
    except ValueError:
        return False

layout = [
    [sg.Text('Latitude: '), sg.InputText('',key='lat', size=(14,1))],
    [sg.Text('Longitude: '), sg.InputText('',key='lon', size=(14,1))],
    [sg.Output(size=(88, 20))],
    [sg.Text('Air Pressure'), sg.InputText('',key='air_pressure',size=(14,1))],
    [sg.Text('Air Quality'), sg.InputText('',key='air_quality',size=(14,1))],
    [sg.Text('Ambient temperature'), sg.InputText('',key='ambient_temp',size=(14,1))],
    [sg.Text('Ground temperature'), sg.InputText('',key='grount_temp',size=(14,1))],
    [sg.Text('Humidity'), sg.InputText('',key='humidity',size=(14,1))],
    [sg.Text('Rainfall'), sg.InputText('',key='rainfall',size=(14,1))],
    [sg.Text('Wind direction'), sg.InputText('',key='wind_direction',size=(14,1))],
    [sg.Text('Wind gust speed'), sg.InputText('',key='wind_gust_speed',size=(14,1))],
    [sg.Text('Wind speed'), sg.InputText('',key='wind_speed',size=(14,1))],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Local weather search', layout)

while True:                             # The Event Loop
    event, values = window.read()
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Submit':
        if isReal(values['lat']) and isReal(values['lon']):
            bs("Searching the closest station...")
            my_weather=get_weather(float(values['lat']), float(values['lon'])) 
            bs("Information about weather:")
            
            # -----------------------
            # Output all paramethers
            # -----------------------
            weather = my_weather[0] 
            keys = list(weather.keys())
            print(keys)
            
            for key in keys:
                values[key] = weather[key]
                if key in window.AllKeysDict:
                    window.FindElement(key).Update(values[key])
                    
            
            # Full output
            print(json.dumps(my_weather[0], indent=4, sort_keys=True))
        elif not isReal(values['lat']):
            sg.Popup("Latitude is invalid. Please enter a number, e.g. 24.12")
        elif values['lat'] is None:
            sg.Popup("Please enter latitude")
        elif not isReal(values['lon']):
            sg.Popup("Longitude is invalid. Please enter a number, e.g. -12.12")
        elif values['lon'] is None:
            sg.Popup("Please enter longitude")
    else:
        sg.Popup("Please enter latitude and longitude")


