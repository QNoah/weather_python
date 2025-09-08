import requests

city_name = "Rotterdam"
country_code = "NL"
state_code = ""
api_key = "5339b820ce54ed0c0b4fa971adf7214b"
#
api = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit=1&appid={api_key}"
# 
#
# # 
def request_temperature(lon, lat):
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}")    
    print(r.text)

def get_location_codes(d): # make a return for this function
    lon = d[0]['lon']
    lat = d[0]['lat']
    print("Succesfully received longitude and latitude")
    return lon, lat
    # request_temperature(lon, lat)

def fetch_api():
    r = requests.get(api) # we've gotta put this in a function for a return.
    if r.status_code != 200:
        print("Something went wrong, try again later!")
        return
    if r.status_code == 200:
        return r.json()

data = fetch_api()
lon, lat = get_location_codes(data)
temperature_information = request_temperature(lon, lat)

# if "__name__" == "__main__":
#     # Here we gotta put something for the menu that questions which temperature we want