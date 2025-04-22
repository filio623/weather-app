import requests
from config import API_KEY, DEFAULT_UNITS

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city_name):
    """
    Fetches weather data for a given city from OpenWeatherMap API.

    Args:
        city_name (str): The name of the city.

    Returns:
        dict: A dictionary containing extracted weather information
              (temp, humidity, desc, wind_speed, city) if successful.
        None: If an error occurs (e.g., city not found, network issue).
    """
    # --- Construct the request ---
    # Parameters for the API request
    params ={
        'q': city_name,
        'appid': API_KEY,
        'units': DEFAULT_UNITS
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        # --- Process the successful response ---
        # The API returns data in JSON format.
        # requests can automatically decode this into a Python dictionary:
        data = response.json()

        # ----> YOUR TASK: Extract data here! <----
        # Example (you need to complete this based on the structure above):
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        city = data['name'] # Get the city name as returned by the API

        # Create a dictionary to return the results
        weather_info = {
            'temperature': temp,
            'humidity': humidity,
            'description': description,
            'wind_speed': wind_speed,
            'city': city
        }
        return weather_info

    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
        return None
    except requests.exceptions.Timeout:
        print("Error: Request timed out")
        return None
    except requests.exceptions.RequestException as err:
        # Handle other network-related errors (DNS errors, connection errors)
        print(f"An error occurred: {err}")
        return None
    except KeyError as key_err:
         # Handle cases where expected keys are missing in the JSON response
         print(f"Error parsing weather data: Missing key {key_err}")
         # print(data) # Optional: print the problematic data structure
         return None
    
if __name__ == '__main__':
    test_city = 'Cairo'
    print(f"fetching weather near {test_city}")
    weather = get_weather_data(test_city)

    if weather:
        print("\nExtracted Weather info")
        # Use .get() for safer access in case a key is missing unexpectedly
        print(f"City: {weather.get('city', 'N/A')}")
        print(f"Temperature: {weather.get('temperature', 'N/A')}°F")
        print(f"Humidity: {weather.get('humidity', 'N/A')}%")
        print(f"Description: {weather.get('description', 'N/A')}")
        print(f"Wind Speed: {weather.get('wind_speed', 'N/A')} mph")
    else:
        print("Failed to retrieve weather data")
