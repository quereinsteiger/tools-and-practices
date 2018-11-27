# -*- coding: utf-8 -*-

import pandas as pd

urls = {"mensa" : "https://www.stw-thueringen.de/deutsch/mensen/einrichtungen/ilmenau/mensa-ehrenberg.html",
        "nano" : "https://www.stw-thueringen.de/deutsch/mensen/einrichtungen/ilmenau/cafeteria-nanoteria.html"}
data = {}

for index, url in urls.items():
    data[index] = pd.read_html(url)    

print("\n\nIn der Mensa gibt es heute: \n")
print(data['mensa'][0][0:].to_string())

print("\n\nIn der Nano gibt es heute: \n")
print(data['nano'][0][0:].to_string())
