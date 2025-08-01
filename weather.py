from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city = "Abuja"):
    requests_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(requests_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***')

    city = input("\nPlease enter a city or location: ")

    if not bool(city.strip()):
        city = "Abuja"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)