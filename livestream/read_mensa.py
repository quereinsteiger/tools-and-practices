#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

urls = {"mensa" : "https://www.stw-thueringen.de/deutsch/mensen/einrichtungen/ilmenau/mensa-ehrenberg.html",
        "nano" : "https://www.stw-thueringen.de/deutsch/mensen/einrichtungen/ilmenau/cafeteria-nanoteria.html"}
data = {}
days = {0: 'heute', 1: 'morgen', 2 : 'übermorgen'}

for index, url in urls.items():
    data[index] = pd.read_html(url)    

for key in urls.keys():
    for index, day in days.items():
        print("\n\nIn der {mensa} gibt es {day}: \n".format( mensa = key, 
                                                             day = day))
        print(data[key][index][0:].to_string())

input()