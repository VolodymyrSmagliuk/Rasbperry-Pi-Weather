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
    print("------------------------------------------------------")
    print(" "+message)
    print("------------------------------------------------------")

def isReal(check):
    try:
        # validate it's a float
        float(check)
        return True
    except ValueError:
        return False

size_layer_2=(14,1)
size_layer_3=(13,2)
size_layer_1=(10,2)

size_progress_bar=(30,10)
size_layer_5=(10,1)
size_output=(88, 10)

layout = [
    [
        sg.Text('Latitude: ', size=size_layer_5),
        sg.InputText('',key='lat', size=size_layer_2)
        ],
    [
        sg.Text('Longitude: ', size=size_layer_5),
        sg.InputText('',key='lon', size=size_layer_2)
        ],
    [
        sg.Text('Progress: ', size=size_layer_5),
        sg.ProgressBar(6, orientation='h', size=size_progress_bar, key='progressbar')
        ],
    [
        sg.Output(size=size_output)],
    [
        sg.Text('Air Pressure', size=size_layer_3),
        sg.InputText('',key='air_pressure', size=size_layer_1),
        sg.Text('Air Quality', size=size_layer_3),
        sg.InputText('',key='air_quality',size=size_layer_1)
        ],
    [
        sg.Text('Ambient temperature', size=size_layer_3),
        sg.InputText('',key='ambient_temp',size=size_layer_1),
        sg.Text('Ground temperature', size=size_layer_3),
        sg.InputText('',key='ground_temp',size=size_layer_1)
        ],
    [
        sg.Text('Humidity', size=size_layer_3),
        sg.InputText('',key='humidity',size=size_layer_1),
        sg.Text('Rainfall', size=size_layer_3),
        sg.InputText('',key='rainfall',size=size_layer_1)
        ],
    [
        sg.Text('Wind direction', size=size_layer_3),
        sg.InputText('',key='wind_direction',size=size_layer_1),
        sg.Text('Wind gust speed', size=size_layer_3),
        sg.InputText('',key='wind_gust_speed',size=size_layer_1),
        sg.Text('Wind speed', size=size_layer_3),
        sg.InputText('',key='wind_speed',size=size_layer_1)
        ],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Local Weather Searcher', layout)

while True:                             # The Event Loop
    event, values = window.read()
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Submit':
        # Check latitude is valid
        if not isReal(values['lat']):
            sg.Popup("Please enter latitude. Latitude should be a number")
        elif float(values['lat']) > 86 or float(values['lat']) < -86:
            sg.Popup("Latitude is invalid. Please enter a number from -85 to 85, e.g. 50.12")
        # Check longitude is valid
        elif not isReal(values['lon']):
            sg.Popup("Please enter longitude. Longitude should be a number")
        elif float(values['lon']) > 181 or float(values['lon']) < -181:
            sg.Popup("Longitude is invalid. Please enter a number from -180 to 180, e.g. -25.12")
        # Check both is valid = main function
        elif isReal(values['lat']) and isReal(values['lon']):
            progress_bar = window.FindElement('progressbar')
            progress_count = 1
            progress_bar.UpdateBar(progress_count+1)
            
            bs("Searching the closest station...")
            progress_bar.UpdateBar(progress_count+1)
            my_weather=get_weather(float(values['lat']), float(values['lon'])) 
            bs("Full Information about weather:")
            progress_bar.UpdateBar(progress_count+1)
            
            # -----------------------
            # Output all paramethers
            # -----------------------
            weather = my_weather[0] 
            keys = list(weather.keys())
            
            for key in keys:
                values[key] = weather[key]
                if key in window.AllKeysDict:
                    window.FindElement(key).Update(values[key])
                    
            print(json.dumps(my_weather[0], indent=4, sort_keys=True))
            progress_bar.UpdateBar(6)
            sg.PopupOK('Finish')

      
    else:
        sg.Popup("Please enter latitude and longitude")


