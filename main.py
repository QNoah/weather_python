import requests

city_name = "Rotterdam"
country_code = "NL"
state_code = ""


api = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit=1&appid=5339b820ce54ed0c0b4fa971adf7214b"