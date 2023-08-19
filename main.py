import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "a6f2d8afb913cd62736bfe0e9b559b48"
CITY = "London"

url = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

response = requests.get(url).json()

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

temp_kelvin = response['main']['temp']
temp_celcius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise']+ response['timezone']) 
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset']+ response['timezone']) 
wind_speed = response['wind']['speed']

print(f"Temperature in {CITY}: {temp_celcius:.0f} degrees Celcius or {temp_fahrenheit:.0f} degrees Fahrenheit")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind speed in {CITY}: {wind_speed}m/s")
print(f"General weather in {CITY}: {description}")
print(f"Sun rises in {CITY} at {sunrise_time}")
print(f"Sun sets in {CITY} at {sunset_time}")
