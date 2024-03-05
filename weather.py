import tkinter as tk
import requests


def get_weather():
    city = city_entry.get()
    api_key = 'YOUR_API_KEY'  # Replace with your API key
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
    response = requests.get(url)
    weather_data = response.json()

    if 'error' not in weather_data:
        weather_description = weather_data['current']['condition']['text']
        temperature = weather_data['current']['temp_c']
        humidity = weather_data['current']['humidity']
        wind_speed = weather_data['current']['wind_kph']
        result_label.config(text=f"Weather: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} km/h")
    else:
        result_label.config(text="City not found. Please enter a valid City.")


# Create the main window
root = tk.Tk()
root.title("Weather App")

# Set the background color of the window
root.config(bg="light blue")

# Set the window size
window_width = 400
window_height = 250
root.geometry(f"{window_width}x{window_height}")

# Disable window resizing
root.resizable(False, False)


# Calculate center positions
center_x = window_width // 2
center_y = window_height // 2

# Create and position widgets
city_label = tk.Label(root, text="Enter City", bg="light blue")
city_label.place(x=center_x - city_label.winfo_reqwidth() // 2, y=center_y - 80)

city_entry = tk.Entry(root)
city_entry.place(x=center_x, y=center_y - 50, anchor="center")

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.place(x=center_x, y=center_y - 10, anchor="center")

result_label = tk.Label(root, text="", bg="light blue")
result_label.place(x=center_x, y=center_y + 50, anchor="center")

# Run the main event loop
root.mainloop()
