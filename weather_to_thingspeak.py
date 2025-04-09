import requests
import time
import os
import warnings
from dotenv import load_dotenv
from requests.exceptions import RequestException

# Suppress specific urllib3 warning
warnings.filterwarnings("ignore", module="urllib3")

# Load environment variables
load_dotenv()

# === CONFIGURATION from .env ===
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
CITY = os.getenv('CITY')
THINGSPEAK_WRITE_API_KEY = os.getenv('THINGSPEAK_WRITE_API_KEY')

def get_weather_data():
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']

        return temperature, humidity, pressure, wind_speed

    except RequestException as e:
        print("Network or HTTP error:", e)
    except KeyError as e:
        print("Unexpected data format from API. Missing key:", e)
    except Exception as e:
        print("General error while fetching weather data:", e)

    return None, None, None, None

def send_to_thingspeak(temp, humidity, pressure, wind_speed):
    try:
        if None in (temp, humidity, pressure, wind_speed):
            print("Invalid data. Skipping upload to ThingSpeak.")
            return

        payload = {
            'api_key': THINGSPEAK_WRITE_API_KEY,
            'field1': temp,
            'field2': humidity,
            'field3': pressure,
            'field4': wind_speed
        }
        response = requests.post("https://api.thingspeak.com/update", params=payload, timeout=10)
        response.raise_for_status()
        print("Data sent to ThingSpeak! Status Code:", response.status_code)

    except RequestException as e:
        print("Failed to send data to ThingSpeak:", e)
    except Exception as e:
        print("Unexpected error during ThingSpeak upload:", e)

if __name__ == "__main__":
    while True:
        temp, humidity, pressure, wind_speed = get_weather_data()
        if all(val is not None for val in (temp, humidity, pressure, wind_speed)):
            print(f"Temp: {temp}°C | Humidity: {humidity}% | Pressure: {pressure} hPa | Wind Speed: {wind_speed} m/s")
        send_to_thingspeak(temp, humidity, pressure, wind_speed)
        time.sleep(600)  # wait 10 minutes