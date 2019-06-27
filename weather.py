import requests, json, time
from config import api_key as YOUR_KEY  

api_key = YOUR_KEY 
def get_location():
    response = requests.get("https://location.services.mozilla.com/v1/geolocate?key=geoclue").json()
    latitude = response["location"]["lat"]
    longitude = response["location"]["lng"]
    return (latitude, longitude)

def get_weather(lat, lon):
    lat, lon = str(lat), str(lon)
    url = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&APPID="+api_key
    data = requests.get(url).json()
    weather = data["weather"]
    main = weather[0]["main"] 
    temp = data["main"]["temp"] -272.15
    print( str(format(temp, ".1f"))+"°C")
    return temp

latitude, longitude = get_location()
get_weather(latitude, longitude)
