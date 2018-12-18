#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

mensen = {"mensa" : "https://www.stw-thueringen.de/deutsch/mensen/einrichtungen/ilmenau/mensa-ehrenberg.html",
          "nano" : "https://www.stw-thueringen.de/deutsch/mensen/einrichtungen/ilmenau/cafeteria-nanoteria.html"}
data = {}
days = {0: 'heute', 1: 'morgen', 2 : 'übermorgen'}

for mensa, url in mensen.items():
    data[mensa] = pd.read_html(url)    

for mensa in data:
    for index, day in days.items():
        print("\n\nIn der {mensa} gibt es {day}: \n".format( mensa = mensa, 
                                                             day = day))
        print(data[mensa][index][0:].to_string())

input()