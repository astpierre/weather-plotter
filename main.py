import os
import sys
import scipy
import pandas
import darksky
import numpy as np
from darksky import forecast
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.dates as mdates
from datetime import datetime as dt

key = "18d9c35760a8c1badc97586c788e0863"

class Location():
    def __init__(self, lat, lon, name):
        self.lattitude = lat
        self.longitude = lon
        self.id = name

class Metric():
    def __init__(self, timestamp, value):
        self.ts = timestamp
        self.val = value

GROTON_HOME = Location(42.594120, -71.508453, "Goton, MA")
PURDUE_UNIV = Location(40.423538, -86.921738, "Purdue University")
SAN_FRANCISCO = Location(37.774929, -122.419418, "San Francisco, CA")

class Weather():
    def __init__(self, location):
        if not isinstance(location, Location):
            raise TypeError("location must be of Location type.")
        else:
            self.id = location.id
            self.lattitude = location.lattitude
            self.longitude = location.longitude
        self.getWeather()

    def getWeather(self):
        self.weather = forecast(key, self.lattitude, self.longitude)
        hourly = self.weather.hourly
        minutely = self.weather.minutely
        hourlyTemps = [ Metric(dt.fromtimestamp(h.time).strftime('%H:%M'),
                               h.temperature) for h in hourly ]
        hourlyPrecipProb = [ Metric(dt.fromtimestamp(h.time).strftime('%H:%M'),
                               h.precipProbability) for h in hourly ]

        fig, ax = plt.subplots()
        plt.subplot(2,1,1)
        plt.title("Temperature by Hour")
        y_vals = [float(h.val) for h in hourlyTemps]
        plt.plot(range(0,49), y_vals)

        plt.subplot(2,1,2)
        plt.title("Precipitation Probability by Hour")
        y_vals = [float(h.val) for h in hourlyPrecipProb]
        plt.plot(range(0,49), y_vals)

        ax.grid(True)
        plt.show()



if __name__ == "__main__":
    grotonWeather = Weather(GROTON_HOME)
