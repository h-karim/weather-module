import requests, json, time
from config import api_key 

icons_mapping = {"01d":"\uf00d",
        "01n":"\uf02e",
        "02d":"\uf002",
        "02n": "\uf086",
        "03n":"\uf041", 
        "03d":"\uf041",
        "04n":"\uf041",
        "04d": "\uf041",
        "09n":"\uf01a",
        "09d":"\uf01a",
        "10d":"\uf008",
        "10n":"\uf028",
        "11d":"\uf010",
        "11n":"\uf03b",
        "13d":"\uf00a",
        "13n":"\uf02a",
        "50d":"\uf003",
        "50n":"\uf04a"}

def get_location():
    while True:
        try:
            response = requests.get("https://location.services.mozilla.com/v1/geolocate?key=geoclue").json()
            break
        except(Exception):
            time.sleep(10)

    latitude = response["location"]["lat"]
    longitude = response["location"]["lng"]
    return (latitude, longitude)

def get_weather(lat, lon):
    lat, lon = str(lat), str(lon)
    url = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&APPID="+api_key
    data = requests.get(url).json()
    weather_data = data["weather"]
    temp = data["main"]["temp"] -272.15
    icon_code = weather_data[0]["icon"]
    icon = icons_mapping[icon_code]
    return [icon, str(format(temp, ".1f")+"°C")]

latitude, longitude = get_location()
weather = get_weather(latitude, longitude)
output = open("variables","w")
print("icon= "+weather[0]+"\n"+"temp= "+weather[1], file=output)
output.close()
print(weather[0], end="")
