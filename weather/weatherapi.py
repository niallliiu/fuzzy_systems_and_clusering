import requests
import json
from datetime import datetime

def get_weather_data(location_lat, location_lon):
    """
    Fetch weather data for a given location using the MET API.
    """
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={location_lat}&lon={location_lon}"
    headers = {
        'User-Agent': 'YourAppName/1.0 (youremail@example.com)'  # Replace with your app name and email
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  # Return the weather data as a JSON object
    else:
        print(f"Error fetching data: {response.status_code}")
        return None  # Return None if the request fails


def save_to_json(data, filename):
    """
    Save data to a JSON file.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data saved to {filename}")


def process_weather_data(weather_data):
    """
    Process weather data into a structured format for easy analysis.
    Extracts time, temperature, weather symbol, and precipitation amount.
    """
    timeseries = weather_data['properties']['timeseries']
    processed_data = []

    # Group by day
    current_day = None
    daily_data = []

    for entry in timeseries:
        timestamp = entry['time']
        instant_data = entry['data']['instant']['details']
        next_1h = entry['data'].get('next_1_hours', {})
        next_1h_summary = next_1h.get('summary', {}).get('symbol_code', "N/A")
        next_1h_precipitation = next_1h.get('details', {}).get('precipitation_amount', 0.0)

        # Parse timestamp
        dt_obj = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        date = dt_obj.strftime('%Y-%m-%d')
        hour = dt_obj.strftime('%H:%M')

        # Check for a new day
        if current_day != date:
            if daily_data:
                processed_data.append({"date": current_day, "entries": daily_data})
            current_day = date
            daily_data = []

        # Add hourly data to the current day's list
        daily_data.append({
            "hour": hour,
            "temperature": instant_data["air_temperature"],
            "weather_symbol": next_1h_summary,
            "precipitation_amount": next_1h_precipitation
        })

    # Add the last day's data
    if daily_data:
        processed_data.append({"date": current_day, "entries": daily_data})

    return processed_data


# Example Usage (coordinates for Råholt, Norway)
location_lat = 63.4305
location_lon = 10.3951

# Fetch weather data
weather_data = get_weather_data(location_lat, location_lon)

if weather_data:
    # Save raw weather data
    save_to_json(weather_data, "weather_data_raw.json")

    # Process and save structured weather data
    processed_data = process_weather_data(weather_data)
    save_to_json(processed_data, "weather_data_processed.json")
else:
    print("Failed to fetch weather data.")
