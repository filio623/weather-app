import tkinter as tk
from tkinter import ttk
from weather_api import get_weather_data

class WeatherGui:

    def __init__(self, root_window):
        self.root = root_window
        self.root.title("Welcome to the weather!")
        self._create_widgets()

    def _create_widgets(self):
        
        input_frame = ttk.Frame(self.root, padding=10)
        input_frame.grid(row=0, column=0, sticky="ew")
        input_frame.columnconfigure(0, weight=1) # Make entry expand

        self.city_label = ttk.Label(input_frame, text='Enter City Name')
        self.city_label.grid(row=0, column=0, padx=5, pady=5)

        self.city_entry = ttk.Entry(input_frame, width=30)
        self.city_entry.grid(row=0, column=1, padx=5, pady=5)
        # Bind the <Return> key (Enter) to the add_task method
        self.city_entry.bind("<Return>", self._handle_get_weather)

        self.get_weather_button = ttk.Button(input_frame, text='Get Weather', command=self._handle_get_weather)
        self.get_weather_button.grid(row=1, column=0, columnspan=2, pady=10)

        results_frame = ttk.Frame(self.root, padding=10)
        results_frame.grid(row=1, column=0, sticky="nsew")

        self.temp_label = ttk.Label(results_frame, text='Temperature: --')
        self.temp_label.grid(row=0, column=0, sticky="w")

        self.humid_label = ttk.Label(results_frame, text='Humidity: --')
        self.humid_label.grid(row=1, column=0, sticky="w")

        self.desc_label = ttk.Label(results_frame, text='Description: --')
        self.desc_label.grid(row=2, column=0, sticky="w")

        self.wind_label = ttk.Label(results_frame, text='Wind Speed: --')
        self.wind_label.grid(row=3, column=0, sticky="w")

    def _handle_get_weather(self, event=None):
        city_name = self.city_entry.get()

        if not city_name:
            self._display_error("Please enter a city name")
            return
        
        weather_data = get_weather_data(city_name)

        if weather_data:
            self._update_display(weather_data)
        else:
            self._display_error(f"Could not fetch weather for {city_name}")

    def _update_display(self, weather_data):

        temp = weather_data.get('temperature', 'N/A')
        humidity = weather_data.get('humidity', 'N/A')
        description = weather_data.get('description', 'N/A').capitalize() # Capitalize description
        wind_speed = weather_data.get('wind_speed', 'N/A')
        city = weather_data.get('city', 'N/A')

        # Update the text of each label using .config() or .configure()
        # Make sure units match what you requested (imperial: °F, mph)
        self.temp_label.config(text=f"Temperature: {temp}°F")
        self.humid_label.config(text=f"Humidity: {humidity}%")
        self.desc_label.config(text=f"Description: {description}")
        self.wind_label.config(text=f"Wind Speed: {wind_speed} mph")

        self.root.title(f"Weather in {city}")

    def _display_error(self, message):
        # Option 1: Display error in the description label & clear others
        self.desc_label.config(text=f"Error: {message}")
        self.temp_label.config(text="Temperature: --")
        self.humid_label.config(text="Humidity: --")
        self.wind_label.config(text="Wind Speed: --")

        # Option 2 (Better): Add a dedicated status label below the results frame
        # and display errors/status there. If you add self.status_label:
        # self.status_label.config(text=message, foreground="red")
        # You might also want a method to clear previous results when an error occurs
        # self._clear_display() # (You would need to write this method)
