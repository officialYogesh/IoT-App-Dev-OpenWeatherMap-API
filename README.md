# IoT Weather Data Visualization using ThingSpeak

## Overview
This project demonstrates a real-time IoT data pipeline that collects weather metrics from the OpenWeatherMap API and visualizes them using ThingSpeak. It simulates an IoT setup where a device (like a Raspberry Pi) gathers environmental data and streams it to a cloud-based IoT analytics platform.

## System Architecture

The system consists of the following components:

- **OpenWeatherMap**: External weather API used to simulate live sensor data.
- **Python Script**: Acts as a virtual IoT device fetching data periodically.
- **ThingSpeak**: IoT cloud platform that stores and visualizes incoming data.

## Step-by-Step Implementation

### Step 1: ThingSpeak Channel Setup
- Created a new ThingSpeak account.
- Set up a new channel with four fields:
  - Field 1: Temperature
  - Field 2: Humidity
  - Field 3: Pressure
  - Field 4: Wind Speed

### Step 2: Get OpenWeatherMap API Key
- Registered at [https://openweathermap.org/](https://openweathermap.org/).
- Retrieved a free API key for accessing current weather data.

### Step 3: Implement Data Retrieval Script
- Wrote a Python script that:
  - Fetches temperature, humidity, pressure, and wind speed every 10 minutes.
  - Sends the data to ThingSpeak using its Write API Key.
  - Handles errors and warning suppression for cleaner logs.

### Step 4: Visualize Weather Data
- Accessed the ThingSpeak dashboard to view auto-generated charts.
- Added individual widgets for each field (temperature, humidity, etc.).
- Used MATLAB Visualization to combine all four metrics into one graph.

## Environment Setup

### Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install required packages:
```bash
pip install -r requirements.txt
```

### Create `.env` file:
```env
OPENWEATHER_API_KEY=your_openweather_api_key
CITY=your_city_name
THINGSPEAK_WRITE_API_KEY=your_thingspeak_write_key
```

## Running the Application
```bash
python weather_to_thingspeak.py
```
The script runs indefinitely, fetching weather data every 10 minutes and pushing it to ThingSpeak.

## Project Structure

```
.
├── .env                  # Environment variables (not checked in)
├── requirements.txt      # Python dependencies
├── weather_to_thingspeak.py  # Main IoT script
└── README.md             # Project documentation
```

## Reflection and Learnings

### Challenges:
- Mapping real-world weather data into an IoT framework
- Understanding ThingSpeak’s structure for multiple field visualizations

### Learnings:
- Gained hands-on experience with IoT data pipelines
- Explored cloud-based visualization tools like ThingSpeak
- Understood the importance of dashboard design in real-time systems

### Personal Insights:
This project demonstrated how easily cloud platforms can simulate and support IoT workflows without needing physical sensors. It highlighted the simplicity and power of ThingSpeak for prototyping and monitoring environmental data.

## Future Enhancements
- Replace API data with actual sensor values from Raspberry Pi or ESP32
- Add email/SMS alerts when weather crosses thresholds
- Integrate data with Google Sheets or Power BI for extended analytics

## Repository
[GitHub Repo](https://github.com/officialYogesh/IoT-App-Dev-OpenWeatherMap-API)
