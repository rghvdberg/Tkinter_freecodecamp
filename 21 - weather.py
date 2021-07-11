# 21 - Build a Weather App
# 22 - 
from tkinter import *
import requests
import json

root = Tk()
root.geometry("400x50")
root.title("Weather App")
root.configure(bg="green")

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=96193FDA-2E4A-4F69-B96F-C49AD7FB6632

try:
    api_request = requests.get(
        "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=96193FDA-2E4A-4F69-B96F-C49AD7FB6632")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = str(api[0]['AQI'])
    category = api[0]['Category']['Name']
except Exception as e:
    api = "Error..."

my_label = Label(root, text=city + " Air Quality " + quality +
                 " " + category, font=("sans", 16), bg="green")
my_label.pack()

root.mainloop()
