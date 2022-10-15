# city temp ranger
Show current temperature and low/high ranges for various cities

![weather.png](weather.png?raw=true "weather.png")

## Goals

* Show the current temperature for various cities
* Show the high / low temperatures for the cities
* Make it easy to compare current temperature and ranges between locations

## Overview

This is a script which generates an image of temperatures of cities of your choice. This is a concept that's been rolling around in my head for a few years now. I primarily used matplotlib and seaborn to generate a single image (with transparent background) which I display on my (mac) desktop with [Übersicht](https://tracesof.net/uebersicht/) like so (in the upper left hand corner):

![desktop](desktop_upper_left.jpg?raw=true "desktop_upper_left.jpg")

## Usage

If you want to use the script as is, you'll have to get an [OpenWeather](https://openweathermap.org) API account to grab the weather (free within limits) and then update the key in the script. You'll also need to install the requirements (mainly pandas, matplotlib, requests, seaborn) with:

    pip install -r requirements.txt

modify the existing list of cities in get_weather.py (arbitrary 3 letter names, not official airport codes). Google lat lons for yourself:

    latlon = {
    'LAS':('36.169941','-115.139832'),
    'NYC':('40.758180','-73.984602'),
    'LDN':('51.507351','0.127758'),
    'BAR':('41.385063','2.173404'),
    'BNG':('12.971599','77.594566'),
    'SEO':('37.5600','126.9900'),
    'SYD':('-33.8650','151.2094')
    }

and then run the script with:

    python get_weather.py
    
which should generate a weather.png

## opportunities

This script could be improved by:

* moving the api key and list of cities into a separate config file. *you should never put secrets directly in code*
* moving color options into a separate config file. (maybe the same as above?)
* creating a set of defaults for a light background as it's currently made more for dark backgrounds
* your pull requests (potentially)
