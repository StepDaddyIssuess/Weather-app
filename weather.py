import tkinter as tk
from tkinter import Entry, Label, Button
from tkinter.messagebox import showerror
from tkinter import PhotoImage, Image
import requests
import datetime as dt
import time

def convert_cel_kel(celsius):
    kelvin = celsius + 273.15
    return kelvin

# Function to convert Kelvin to Celsius
def convert_cel_far(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

def get_weather(city):
    api_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=82667ab975ff6e667b4316202b85eff8&units=metric'.format(city)

    res = requests.get(api_url)
    data = res.json()

    #feels_like
    temp_feels = data['main']['feels_like']
    feri_feels = convert_cel_far(temp_feels)
    kel_feels = convert_cel_kel(temp_feels)

    #Temperature
    cel = data['main']['temp']
    feri = convert_cel_far(cel)
    kel = convert_cel_kel(cel)

    #Changes
    frame.config(relief="solid")
    frame.pack(pady=5, anchor="s")

    feels_like_label.config(text=f"Feels like:          Tempetarue: \n{int(temp_feels)}C°                         {int(cel)}C°\n{int(feri_feels)}F°                         {int(feri)}F°\n{int(kel_feels)}K°                         {int(kel)}K°") 

    wind_label.config(text=f"Wind: {data['main']['pressure']}")
    description_label.config(text=f"Description: {data['weather'][0]['description']}")
    humidity_label.config(text=f"Humidity: {data['main']['humidity']}%")
    sunrise_label.config(text=f"Sunrise: {dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])}")
    sunset_label.config(text=f"Sunset: {dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])}")

    try:
        if data['weather'][0]['description'] == "scattered clouds" or "broken clouds" or "overcast clouds":
            images = PhotoImage(file="cloudy.png")
            image_label.config(image=images)
            image_label.image = images
            image_label.pack()

        elif "snow" in data['weather'][0]['description']:
            images = PhotoImage(file="snow.png")
            image_label.config(image=images)
            image_label.image = images
            image_label.pack()

        elif data['weather'][0]['description'] == "clear sky":
            images = PhotoImage(file="sun.png")
            image_label.config(image=images)
            image_label.image = images
            image_label.pack()

        elif data['weather'][0]['description'] == "rain" or data['weather'][0]['description'] == "light rain" or data['weather'][0]['description'] == "moderate rain" or data:
            images = PhotoImage(file="rain.png")
            image_label.config(image=images)
            image_label.image = images
            image_label.pack()

        elif data['weather'][0]['description'] == "thunderstorm":
            images = PhotoImage(file="lightning.png")
            image_label.config(image=images)
            image_label.image = images
            image_label.pack()

    except Exception as e:
        tk.messagebox.showerror("Error", "An error occurred")
    


def get_weather_from_input():
    city = city_entry.get()
    try:
        get_weather(city)
    except Exception as e:
        tk.messagebox.showerror("Error", f"An error occurred: City not found")

def update_and_sleep():
    print("updated")
    get_weather(city_entry.get())
    root.after(60000, update_and_sleep)
# Create main window
root = tk.Tk()
root.title("Weather App")
root.geometry("600x600")
root.config(bg="#246EE9")


# Create and place widgets
city_label = Label(root, text="Enter city:", font=("Arial", 16, "bold"), bg="#add8e6")
city_label.pack(pady=10)

city_entry = Entry(root, font=("Arial", 16, "bold"), bg="#add8e6")
city_entry.pack(pady=10)

get_weather_button = Button(root, text="Get Weather", command=get_weather_from_input, font=("Arial", 10, "bold"), bg="#add8e6")
get_weather_button.pack(pady=10)

#images
image_label = Label(root, )
image_label.pack_forget()


# Frame for the weather data

frame = tk.Frame(root,borderwidth=3, height=500)
frame.pack_forget()

feels_like_label = Label(frame, text="", font=("Arial", 10, "bold"))
feels_like_label.pack()

wind_label = Label(frame, text="", font=("Arial", 10, "bold"))
wind_label.pack()

description_label = Label(frame, text="", font=("Arial", 10, "bold"))
description_label.pack()

humidity_label = Label(frame, text="", font=("Arial", 10, "bold"))
humidity_label.pack()

sunrise_label = Label(frame, text="", font=("Arial", 10, "bold"))
sunrise_label.pack()

sunset_label = Label(frame, text="", font=("Arial", 10, "bold"))
sunset_label.pack()

temperature_label = Label(frame, text="", font=("Arial", 10, "bold"))
temperature_label.pack()


root.after(60000, update_and_sleep)

root.mainloop()
