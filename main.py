from PySimpleGUI import PySimpleGUI as sg # import main GUI module
from FindClosest import find_closest # import muself function to search closest station
import json # import json processer
from requests import get # import get library
from pprint import pprint # import updated print()

def get_weather(my_lat, my_lon):  # get current weather
    weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/' # find weather by id of station
    closest_stn = find_closest(my_lat, my_lon) # id of closest station
    weather = weather + str(closest_stn) # convert int to string
    my_weather = get(weather).json()['items'] # send GET request
    return my_weather # return metrics

def bs(message): # beautiful separate
    print("------------------------------------------------------")
    print(" "+message)
    print("------------------------------------------------------")

def isReal(check): # checker
    try: 
        float(check) # validate it's a float
        return True # float
    except ValueError: # check type of error
        return False # not float - statement or something

size_layer_2=(14,1) # main text
size_layer_3=(13,2) # for metrics
size_layer_1=(10,2) # for metrics
size_progress_bar=(30,10) # progress bar mesurments
size_layer_5=(10,1) # main inputs
size_output=(88, 10) # output section

layout = [ # layouts
    [ # Layer 1
        sg.Text('Latitude: ', size=size_layer_5), # text layer for latitude
        sg.InputText('',key='lat', size=size_layer_2) # input layer for latitude
    ],
    [ # Layer 2
        sg.Text('Longitude: ', size=size_layer_5), # text layer for longitude
        sg.InputText('',key='lon', size=size_layer_2) # input layer for longitude
    ],
    [ # Layer 3
        sg.Text('Progress: ', size=size_layer_5), # text layer for progress
        sg.ProgressBar(6, orientation='h', size=size_progress_bar, key='progressbar') # visual layer for progress
    ],
    [ # Layer 4
        sg.Output(size=size_output)], # output layer
    [ # Layer 5
        sg.Text('Air Pressure', size=size_layer_3), # text layer for air pressure
        sg.InputText('',key='air_pressure', size=size_layer_1), # input layer for air pressure
        sg.Text('Air Quality', size=size_layer_3), # text layer for air quality
        sg.InputText('',key='air_quality',size=size_layer_1) # input layer for air quality
    ],
    [ # Layer 6
        sg.Text('Ambient temperature', size=size_layer_3), # text layer for ambient temperature
        sg.InputText('',key='ambient_temp',size=size_layer_1), # input layer for ambient temperature
        sg.Text('Ground temperature', size=size_layer_3), # text layer for Ground temperature
        sg.InputText('',key='ground_temp',size=size_layer_1) # input layer for Ground temperature
    ],
    [ # Layer 7
        sg.Text('Humidity', size=size_layer_3), # text layer for humidity
        sg.InputText('',key='humidity',size=size_layer_1), # input layer for humidity
        sg.Text('Rainfall', size=size_layer_3), # text layer for rainfall
        sg.InputText('',key='rainfall',size=size_layer_1) # input layer for rainfall
    ],
    [ # Layer 8
        sg.Text('Wind direction', size=size_layer_3), # text layer for wind direction
        sg.InputText('',key='wind_direction',size=size_layer_1), # input layer for wind direction
        sg.Text('Wind gust speed', size=size_layer_3), # text layer for wind gust speed
        sg.InputText('',key='wind_gust_speed',size=size_layer_1), # input layer for wind gust speed
        sg.Text('Wind speed', size=size_layer_3), # text layer for wind speed
        sg.InputText('',key='wind_speed',size=size_layer_1) # input layer for wind speed
    ],
    [sg.Submit(), sg.Cancel()]  # Layer 9 - Submit and Cansel buttons
]

window = sg.Window('Local Weather Searcher', layout) # create window 

while True:                             # The Event Loop
    event, values = window.read()   # import parameters from layout
    if event in (None, 'Exit', 'Cancel'): # if click EXIT or CANSEL
        break # to stop program 
    if event == 'Submit': # if click SUBMIT
        # -----------------------Latitude---------------------------
        if not isReal(values['lat']): # Check latitude is valid and exists
            sg.Popup("Please enter latitude. Latitude should be a number") # window "warning" pop up message
        elif float(values['lat']) > 86 or float(values['lat']) < -86: # range of enabled values
            sg.Popup("Latitude is invalid. Please enter a number from -85 to 85, e.g. 50.12") # window "warning" pop up message
        # -----------------------Longitude---------------------------
        elif not isReal(values['lon']): # Check longitude is valid and exists
            sg.Popup("Please enter longitude. Longitude should be a number") # window "warning" pop up message
        elif float(values['lon']) > 181 or float(values['lon']) < -181: # range of enabled values
            sg.Popup("Longitude is invalid. Please enter a number from -180 to 180, e.g. -25.12") # window "warning" pop up message
        # -----------------------Main---------------------------
        elif isReal(values['lat']) and isReal(values['lon']): # check both lat and lon are numbers
            # -----------------------Progress Bar---------------------------
            progress_bar = window.FindElement('progressbar') # attach progress_bar element
            progress_count = 1 # current progress_bar progress
            progress_bar.UpdateBar(progress_count+1) # increase progress_bar progress
            # -----------------------Weather---------------------------
            bs("Searching the closest station...") # action in progress
            progress_bar.UpdateBar(progress_count+1) # update progress
            my_weather=get_weather(float(values['lat']), float(values['lon'])) # load closest weather
            bs("Full Information about weather:") # output full inforation
            progress_bar.UpdateBar(progress_count+1) # update progress
            weather = my_weather[0] # use first dictionary of list
            keys = list(weather.keys()) # write all keys of dictionary
            for key in keys: # create loop
                values[key] = weather[key] # write value from Oracle DB to value of specific input layer
                if key in window.AllKeysDict: # check is input layer exists
                    window.FindElement(key).Update(values[key]) # update value of input layer
            # -----------------------Print full information---------------------------
            print(json.dumps(my_weather[0], indent=4, sort_keys=True)) # use json.dumps for pretty output of json
            progress_bar.UpdateBar(6) # process DONE
            sg.PopupOK('Finish') # message about finish
    else: # exception
        sg.Popup("Please enter latitude and longitude") # else message