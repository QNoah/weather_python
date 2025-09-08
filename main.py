import requests
import json

city_name = "Rotterdam"
country_code = "NL"
state_code = ""
lon = ""
lat = ""
api = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit=1&appid=5339b820ce54ed0c0b4fa971adf7214b"
#this one ^ is important to receive the latitude and longitude. with that another request should be done to get the temperature.
#
# 
# 
# https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid={API key}
# this one is important to get temperature ^^  
#

def get_location_codes(d):
    lon = d[0]['lon']
    lat = d[0]['lat']
    print("Succesfully received longitude and latitude")
    # request_temperature()

r = requests.get(api)
if r.status_code != 200:
    print("Something went wrong, try again later!")
if r.status_code == 200:
    data = r.json()
    get_location_codes(data)



    # Ik was gebleven met het ophalen van latitude en longitude