import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric',  # You can change this to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data['message']}")
            return None
    except requests.ConnectionError:
        print("Failed to connect to the weather API. Please check your internet connection.")
        return None

def display_weather(weather_data):
    if weather_data:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']

        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description.capitalize()}")
    else:
        print("Weather data not available.")

def main():
    api_key = '4b56a6fbdba3810f219d969aab78ed38'  # Replace with your OpenWeatherMap API key
    location = input("Enter city or ZIP code: ")

    weather_data = get_weather(api_key, location)

    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
