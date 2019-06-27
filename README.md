# weather-module
A custom weather module for [Polybar](https://polybar.github.io/)

This module is designed to display location based weather information from OpenWeather using python.
At this moment, the module only displays the current temperature ,further work will be done to add more features and info.

## Setup
To use this module, you need an API key, get it from: https://openweathermap.org/price The free version is enough.
- Make sure you have Python 3.7.3 or later installed
- Install the ```requests``` module if you don't via ```pip install```
- Clone this repository
- Create a ```config.py``` file inside the repo and add ```api_key= <your api key>``` then save it
- In your Polybar config file, add the following:  

``` 
[module/weather]
type=custom/script
interval=3600  #interval in seconds, change it to whatever you see fit
exec= python /path/to/weather.py
```
- Make sure you include the module in one of your modules variables 
