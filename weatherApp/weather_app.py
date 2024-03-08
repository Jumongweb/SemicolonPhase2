import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
#API_KEY = open('api_key', 'r').read()
API_KEY = "4b7c1eb6aad3c6d00ef104248ade6a9c"

CITY = "Lagos"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

print(response)