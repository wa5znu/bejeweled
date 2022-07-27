# https://bigl.es/friday-fun-micro-weather-station/

import network
import time
#import urequests
from machine import Pin
from neopixel import NeoPixel
#from secrets import SSID, PW # secrets.py file contains Wi-Fi details
from random import randint, choice

from demo import Demo

WEATHER_REPORTS = ["Clear", "Clouds", "Rain", "Thunderstorm", "Snow", None]

class WeatherIcons(Demo):
    #Weather Icons
    icon_displaylists = {
        'sun' : ([2,6,7,8,10,11,12,13,14,16,17,18,22], (255,255,0)),
        'cloudy' : ([7,11,12,13,15,16,17,18,19], (8,8,8)),
        'rain_cloud' : ([7,11,12,13,15,16,17,18,19], (8,8,8)),
        'rain1' : ([0,4,5,9,10,12,14,17,22], (0,8,8)),
        'rain2' : ([2,7,10,12,14,15,19,20,24], (0,8,8)),
        'lightning_cloud' : ([2,6,7,8,10,11,12,13,14,16,18,20,22], (8,8,8)),
        'lightning' : ([3,7,11,12,13,17,21], (8,8,0)),
        'snow_ice' : ([0,2,4,7,10,11,12,13,14,17,20,22,24], (0,8,8)),
        'fail' : ([0,4,6,8,12,16,18,20,24], (128,0,0)),
        'fail2' : ([2,7,10,11,12,13,14,17,22], (128,0,0)),
    }

    def __init__(self, np):
        self.np = np
        
        self.weather_table = {
            "Clear": self.sun,
            "Clouds": self.clouds,
            "Rain": self.rain,
            "Thunderstorm": self.thunderstorm,
            "Snow": self.snow,
            None: self.no_weather
        }
        
        assert all(w in self.weather_table for w in WEATHER_REPORTS)

    def draw(self, weather):
        self.weather_table.get(weather, self.no_weather)()

    def draw_icon(self, name):
        (indices, value) = self.icon_displaylists[name]
        for ix in indices:
            self.np[ix] = value
        self.np.write()

    def clear_icon(self, seconds):
        time.sleep(seconds)
        self.np.fill((0,0,0))
        self.np.write()

    def sun(self):
        self.draw_icon('sun')
        self.clear_icon(3)

    def clouds(self):
        self.draw_icon('cloudy')
        self.clear_icon(3)

    def rain(self):
        self.draw_icon('rain_cloud')
        self.clear_icon(0.5)
        for i in range(4):
            self.draw_icon('rain1')
            self.clear_icon(0.5)
            self.draw_icon('rain2')
            self.clear_icon(0.5)

    def thunderstorm(self):
        for i in range(5):
            self.draw_icon('lightning_cloud')
            self.clear_icon(0.5)
            self.draw_icon('lightning')
            self.clear_icon(0.5)

    def snow(self):
        self.draw_icon('snow_ice')
        self.clear_icon(3)

    def no_weather(self):
        for i in range(10):
            self.draw_icon('fail')
            self.clear_icon(0.5)
            self.draw_icon('fail2')
            self.clear_icon(0.5)

class Weather(Demo):
    def __init__(self, np):
        super().__init__(np)
        self.wlan = None
        self.weather_icons=WeatherIcons(np)

    def connect(self):
        #Wi-Fi Setup
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.connect(SSID, PW)
        time.sleep(5)
        print(self.wlan.isconnected())
        print(self.wlan.ifconfig())
        if self.wlan.isconnected() == True:
            for i in range(3):
                self.np.fill((0,16,0))
                self.np.write()
                time.sleep(0.1)
                self.np.fill((0,0,0))
                self.np.write()
                time.sleep(0.1)
        else:
            for i in range(3):
                self.np.fill((16,0,0))
                self.np.write()
                time.sleep(0.1)
                self.np.fill((0,0,0))
                self.np.write()
                time.sleep(0.1)
        time.sleep(3)
    def loop(self, ntimes):
        # just loop once and ignore ntimes
        #Get the weather data
        if self.wlan is not None:
            r = urequests.get("http://api.openweathermap.org/data/2.5/weather?q=Blackpool,UK&appid=--YOUR OPEN WEATHER API KEY HERE--").json()
            weather = r["weather"][0]["main"]
        else:
            #Change the weather here to test the conditional tests.
            weather = choice(WEATHER_REPORTS)

        print(f"weather is {weather}")
        self.weather_icons.draw(weather)

        time.sleep(1)

    
# Happy Hacking!
