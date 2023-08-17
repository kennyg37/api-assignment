import sys
import requests

def get_weather(city_name):
    url = "https://openweather43.p.rapidapi.com/forecast"
    querystring = {
        "appid": "da0f9c8d90bde7e619c3ec47766a42f4",
        "q": city_name,
        "units": "standard"
    }
    headers = {
        "X-RapidAPI-Key": "09220122d7msh9fe81301a1cd7afp1d274djsndd3aaf88202b",
        "X-RapidAPI-Host": "openweather43.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

def print_weather_data(city_name, weather_data):
    try:
        main_data = weather_data['list'][0]['main']
        temperature = main_data['temp']
        humidity = main_data['humidity']
        
        weather_description = weather_data['list'][0]['weather'][0]['description']
        wind_speed = weather_data['list'][0]['wind']['speed']
        clouds = weather_data['list'][0]['clouds']['all']
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description}")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Cloud Coverage: {clouds}%")
    except KeyError:
        print("Error: Unable to fetch weather information.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python weather_app.py <city_name>")
        sys.exit(1)

    city_name = sys.argv[1]
    weather_data = get_weather(city_name)
    print_weather_data(city_name, weather_data)

if __name__ == "__main__":
    main()
