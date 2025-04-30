import requests
from pprint import pprint

API_KEY  = 'a8e58c00b27a31d2cee71bf0fd49ca43'
city  = input("Enter the city name to check weather: ")
base_url = 'http://api.openweathermap.org/data/2.5/weather?appid='+API_KEY+'&q='+city

weather_data = requests.get(base_url).json()
pprint(weather_data)