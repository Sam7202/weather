import requests
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import ssl

#some special weather add emoji
def weather_type(description):
    if description == "clear sky":
        return "clear sky🌞"
    elif description == "few clouds":
        return "few clouds🌤️"
    elif description == "scattered clouds":
        return "scattered clouds🌥️"
    elif description == "broken clouds":
        return "broken clouds🌤️"
    elif description == "shower rain":
        return "shower rain🌧️"
    elif description == "rain":
        return "rain🌧️"
    elif description == "thunderstorm":
        return "thunderstorm🌩️"
    elif description == "snow":
        return "snow🌨️"
    elif description == "mist":
        return "mist🌫️"
    else:
        return description

def temp_feel(temp):
    if temp < 10:
        return "cold🥶"
    elif temp < 20:
        return "cool🤧"
    elif temp < 25:
        return "nice😊"
    elif temp < 30:
        return "hot🥵"
    else:
        return "freaking hot🔥"

def get_weather(api_key):
    # get IP location information
    ip_url = "https://ipapi.co/json/"
    response = requests.get(ip_url)
    if response.status_code == 200:
        location_data = response.json()
        lat = location_data['latitude']
        lon = location_data['longitude']
        city = location_data['city']
    else:
        print("Failed to get location information")
        return

    # get weather data using OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=en"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        print(f"Current Location: {city}")
        print(f"Weather: {weather_type(description)}")
        print(f"Temperature: {temp}°C, {temp_feel(temp)}")
        print(description)
    else:
        print("Failed to get weather data, please check your API key.")

#main function
# replace with your OpenWeatherMap API key
# get in https://openweathermap.org/
api_key = "YOUR_KEY"
get_weather(api_key)
