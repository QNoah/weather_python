import requests
api_key = "5339b820ce54ed0c0b4fa971adf7214b"
api = ""
# 
#
# # 
def request_temperature(lon, lat):
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}")    
    return r.json()


def get_location_codes(d):
    lon = d[0]['lon']
    lat = d[0]['lat']
    print("Succesfully received longitude and latitude")
    return lon, lat


def fetch_api():
    r = requests.get(api)
    if r.status_code != 200:
        print("Something went wrong, try again later!")
        return
    if r.status_code == 200:
        return r.json()


def enter_location() -> str:
    city_name = input("Enter your city name: ")
    country_code = input("Enter your country (Format: NL, USA, ENG, DE): ")
    state_code = input("Enter your state code (leave empty if you are not sure!): ")
    return f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit=1&appid={api_key}"


api = enter_location()
data = fetch_api()
lon, lat = get_location_codes(data)
information = request_temperature(lon, lat)

print(information['main']['temp'])