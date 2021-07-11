# just checking what's actually in the returend data of 
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=96193FDA-2E4A-4F69-B96F-C49AD7FB6632

foo = [
    {
        "DateObserved":"2021-07-10 ",
        "HourObserved":10,
        "LocalTimeZone":"PST",
        "ReportingArea":"Las Vegas",
        "StateCode":"NV",
        "Latitude":36.206,
        "Longitude":-115.223,
        "ParameterName":"O3",
        "AQI":54,
        "Category":
        {
            "Number":2,
            "Name":"Moderate"
        }
    },
    {
        "DateObserved":"2021-07-10 ",
        "HourObserved":10,
        "LocalTimeZone":"PST",
        "ReportingArea":"Las Vegas",
        "StateCode":"NV",
        "Latitude":36.206,
        "Longitude":-115.223,
        "ParameterName":"PM2.5",
        "AQI":48,
        "Category":
        {
            "Number":1,
            "Name":"Good"
        }
    },
    {
        "DateObserved":"2021-07-10 ",
        "HourObserved":10,
        "LocalTimeZone":"PST",
        "ReportingArea":"Las Vegas",
        "StateCode":"NV","Latitude":36.206,
        "Longitude":-115.223,
        "ParameterName":"PM10",
        "AQI":45,"Category":
        {
            "Number":1,
            "Name":"Good"
        }
    }
]

print(foo[0])