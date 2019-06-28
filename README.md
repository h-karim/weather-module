# weather-module
A custom weather module for [Polybar](https://polybar.github.io/)

This module is designed to display location based weather information from OpenWeather using python.
At this moment, the module only displays the current temperature and a weather icon

## Setup
To use this module, an OpenWeather API key is needed, available [here](https://openweathermap.org/price). The free version is enough.
- install the ttf weather icons font:
  - AUR (arch linux): ```yay ttf-weather-icons```      
  - Or manually from https://github.com/erikflowers/weather-icons if they're not present for your distro
- Make sure Python 3.7.3 or later is installed
- Install the ```requests``` module if it's not present via ```pip install```
- Clone this repository
- Create a ```config.py``` file inside the repo and add ```api_key= <your api key>``` then save it
## Polybar formatting 
- In Polybar's config file, a the weather font needs to be added to the list of fonts: ```font-N = Weather Icons:size=12;1```  
- Then create a custom script module:
``` 
[module/weather]
type=custom/script
;interval in seconds, change it accordingly
interval=900  
exec= python /path/to/weather.py
include-file= /path/to/variables_file 
format-suffix= ${self.temp}
;weather icon: replace N by the font number+1 (due to 1 indexing) 
format= %{F#9f78e1}%{TN}<label>
```
- Make sure to include the module in one of the modules variables 
