import requests
import json

def fetch_weather_data(location):
    api_key = '3e0e264c9728760c8fbd9ceea912b41c'  # Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data.")
        return None

def display_weather_data(data):
    if data:
        print("Current Weather in", data['name'], ", ", data['sys']['country'])
        print("Temperature:", data['main']['temp'], "°C")
        print("Humidity:", data['main']['humidity'], "%")
        print("Weather Condition:", data['weather'][0]['description'])
    else:
        print("No weather data available.")

def main():
    location = input("Enter city name or ZIP code: ")
    weather_data = fetch_weather_data(location)
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()
