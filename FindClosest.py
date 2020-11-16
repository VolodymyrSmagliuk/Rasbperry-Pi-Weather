from requests import get # import get library
import json # import json processing
from pprint import pprint # import updated print()
from haversine import haversine # import function to calculate diff between stations

def find_closest(my_latitude, my_longitude): # start function 
  stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations' # GET request - all station
  all_stations = get(stations).json()['items'] # parse list of stations
  smallest = 20036 # the biggest possible  distance - Earth radious
  for station in all_stations: # for loop to find closest station
    station_longitude = station['weather_stn_long'] # write down longitude of station to variable
    station_latitude = station['weather_stn_lat'] # write down latitude of station to variable
    distance = haversine(my_longitude, my_latitude, station_longitude, station_latitude) # distance between two points
    if distance < smallest: # conditional for the smallest distance
        smallest = distance # if true reset smallest by distance
        closest_station = station['weather_stn_id'] # if true rewrite station id
  return closest_station # return id of the closest station