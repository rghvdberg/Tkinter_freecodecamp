# 21 - Build a Weather App
# 22 - Change Colors In our Weather App
# 23 - Add Zipcode Lookup Form

# source https://docs.airnowapi.org/aq101
# 0   - 50 	Good 	                       Green  (00e400) 	1
# 51  - 100 Moderate 	                   Yellow (ffff00) 	2
# 101 - 150 Unhealthy for Sensitive Groups Orange (ff7e00) 	3
# 151 - 200 Unhealthy 	                   Red 	  (ff0000) 	4
# 201 - 300 Very Unhealthy 	               Purple (8f3f97) 	5
# 301 - 500 Hazardous 	                   Maroon (7e0023) 	6


from tkinter import *
import requests
import json

root = Tk()
root.geometry("400x100")
root.title("Weather App")

weather_colors = [
    '#00e400',
    '#ffff00',
    '#ff7e00',
    '#ff0000',
    '#8f3f97',
    '#7e0023',
]
root.configure(bg=weather_colors[0])


def zipLookUp():
    try:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="
            + zip_entry.get() + "&distance=5&API_KEY=96193FDA-2E4A-4F69-B96F-C49AD7FB6632")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = str(api[0]['AQI'])
        category = api[0]['Category']['Name']
        category_number = api[0]['Category']['Number']
        back_ground = weather_colors[category_number - 1]
        root.configure(bg=back_ground)
        my_label = Label(root, text=city + " Air Quality " + quality +
                         " " + category, font=("sans", 16), bg=back_ground)
        my_label.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error..."

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=96193FDA-2E4A-4F69-B96F-C49AD7FB6632

zip_entry = Entry(root)
zip_entry.grid(row=0, column=0, padx=10,pady=10)

zipButton = Button(root, text="Lookup Zipcode", command=zipLookUp)
zipButton.grid(row=0, column=1)

root.mainloop()
