# Python Tkinter Weather App

A simple desktop weather application built with Python and Tkinter that fetches and displays current weather conditions for a specified city using the OpenWeatherMap API.

## Features

* Enter a city name to get current weather data.
* Displays temperature, humidity, weather description, and wind speed.
* Fetches data using the OpenWeatherMap API.
* Basic error handling for invalid city names or network issues.
* User interface built with Tkinter.
* Supports fetching data by pressing Enter in the city field or clicking the "Get Weather" button.

## Screenshot

*(Optional: Add a screenshot of your application window here)*
`![Weather App Screenshot](path/to/your/screenshot.png)`

## Technologies Used

* Python 3.x
* Tkinter (Python's standard GUI library)
* Requests library (for making HTTP API calls)
* OpenWeatherMap API (for weather data)

## Setup and Installation

1.  **Clone the repository (or download the source code):**
    ```bash
    git clone <your-repository-url>
    cd weather-app
    ```

2.  **Create and activate a virtual environment (Recommended):**
    * On macOS/Linux:
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```
    * On Windows:
        ```bash
        python -m venv .venv
        .\.venv\Scripts\activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(This will install the `requests` library).*

4.  **Configure API Key:**
    * Sign up for a free API key at [OpenWeatherMap.org](https://openweathermap.org/appid).
    * Make a copy of the example configuration file: `cp config.py.example config.py` (or copy manually).
    * Open the new `config.py` file in a text editor.
    * Replace the placeholder `"YOUR_OPENWEATHERMAP_API_KEY_HERE"` with your actual OpenWeatherMap API key.
    * **Important:** The `config.py` file is included in `.gitignore` to prevent accidentally committing your secret API key.

## Usage

1.  Make sure your virtual environment is activated.
2.  Run the main application script from the project's root directory:
    ```bash
    python main.py
    ```
3.  The application window will appear.
4.  Enter a city name into the input field.
5.  Press the `Enter` key or click the "Get Weather" button.
6.  The current weather conditions for that city will be displayed.

## Future Improvements

* Add a status bar for better user feedback (e.g., "Fetching...", "Error: City not found").
* Implement unit selection (Metric/Imperial) via radio buttons.
* Display more weather details (e.g., "Feels like" temperature, pressure).
* Improve visual styling of the GUI.
* Add unit tests for the API fetching logic.

