from requests import get # import get library
import json # import json processing
from pprint import pprint # import updated print()
from haversine import haversine # import function to calculate diff between stations

#weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

# my_lat = 50.29007 # my latitude
# my_lon = 25.37424 # my longitude

# all_stations = get(stations).json()['items']

def find_closest(my_latitude, my_longitude): # start function 
  stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
  all_stations = get(stations).json()['items']
  smallest = 20036 # the biggest possible  distance
  for station in all_stations: # for loop to find closest station
    station_longitude = station['weather_stn_long'] # write down longitude of station to variable
    station_latitude = station['weather_stn_lat'] # write down latitude of station to variable
    distance = haversine(my_longitude, my_latitude, station_longitude, station_latitude) # distance between two points
    if distance < smallest: # conditional for the smallest distance
        smallest = distance # if true reset smallest by distance
        closest_station = station['weather_stn_id'] # if true rewrite station id
  return closest_station # return id of the closest station

#closest_stn = find_closest(my_lat, my_lon) # call function and save result to variable
#weather = weather + str(closest_stn) # convert int to string
#my_weather = get(weather).json()['items'] # send GET request
#pprint(my_weather) # print metrics to stdout (terminal)